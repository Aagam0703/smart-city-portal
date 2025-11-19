// Smart City Portal Main JavaScript

class SmartCityPortal {
    constructor() {
        this.init();
    }

    init() {
        this.initializeEventListeners();
        this.loadInitialData();
        this.startAutoRefresh();
    }

    initializeEventListeners() {
        // Navigation active state
        const currentPath = window.location.pathname;
        document.querySelectorAll('.nav-link').forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('active');
            }
        });

        // Dashboard card interactions
        document.querySelectorAll('.dashboard-card').forEach(card => {
            card.addEventListener('click', this.handleCardClick.bind(this));
        });

        // Search functionality
        const searchInput = document.getElementById('dashboardSearch');
        if (searchInput) {
            searchInput.addEventListener('input', this.handleSearch.bind(this));
        }

        // Refresh button
        const refreshBtn = document.getElementById('refreshData');
        if (refreshBtn) {
            refreshBtn.addEventListener('click', this.refreshData.bind(this));
        }
    }

    handleCardClick(event) {
        const card = event.currentTarget;
        const metric = card.dataset.metric;
        
        if (metric) {
            this.showMetricDetails(metric);
        }
    }

    handleSearch(event) {
        const searchTerm = event.target.value.toLowerCase();
        const cards = document.querySelectorAll('.dashboard-card');
        
        cards.forEach(card => {
            const title = card.querySelector('.card-header').textContent.toLowerCase();
            const content = card.textContent.toLowerCase();
            
            if (title.includes(searchTerm) || content.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    async loadInitialData() {
        try {
            // Load quick stats
            await this.loadQuickStats();
            
            // Load recent alerts
            await this.loadRecentAlerts();
            
            // Update last refreshed time
            this.updateLastRefreshed();
            
        } catch (error) {
            console.error('Error loading initial data:', error);
            this.showError('Failed to load dashboard data');
        }
    }

    async loadQuickStats() {
        // Simulate API call - replace with actual endpoints
        const stats = {
            active_alerts: 12,
            total_requests: 156,
            avg_response_time: '2.1h',
            system_status: 'Operational'
        };

        this.updateStatsDisplay(stats);
    }

    async loadRecentAlerts() {
        // Simulate recent alerts data
        const alerts = [
            { type: 'warning', message: 'High traffic congestion in downtown area', time: '5 min ago' },
            { type: 'info', message: 'Weather advisory: Light rain expected', time: '15 min ago' },
            { type: 'success', message: 'Power restored in north district', time: '1 hour ago' }
        ];

        this.updateAlertsDisplay(alerts);
    }

    updateStatsDisplay(stats) {
        Object.keys(stats).forEach(stat => {
            const element = document.getElementById(`stat-${stat}`);
            if (element) {
                element.textContent = stats[stat];
            }
        });
    }

    updateAlertsDisplay(alerts) {
        const container = document.getElementById('recent-alerts');
        if (!container) return;

        container.innerHTML = alerts.map(alert => `
            <div class="alert alert-${alert.type} alert-dismissible fade show" role="alert">
                ${alert.message}
                <small class="text-muted">${alert.time}</small>
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        `).join('');
    }

    async refreshData() {
        const refreshBtn = document.getElementById('refreshData');
        if (refreshBtn) {
            refreshBtn.disabled = true;
            refreshBtn.innerHTML = '<span class="loading"></span> Refreshing...';
        }

        try {
            await this.loadInitialData();
            
            // Show success feedback
            this.showToast('Data refreshed successfully', 'success');
            
        } catch (error) {
            this.showToast('Error refreshing data', 'error');
        } finally {
            if (refreshBtn) {
                refreshBtn.disabled = false;
                refreshBtn.innerHTML = 'Refresh Data';
            }
        }
    }

    startAutoRefresh() {
        // Auto-refresh every 5 minutes
        setInterval(() => {
            this.refreshData();
        }, 5 * 60 * 1000);
    }

    updateLastRefreshed() {
        const element = document.getElementById('last-refreshed');
        if (element) {
            const now = new Date();
            element.textContent = now.toLocaleTimeString();
        }
    }

    showMetricDetails(metric) {
        // Implement metric detail modal or navigation
        console.log('Showing details for metric:', metric);
        
        // Example: Show a modal with detailed information
        // This would be implemented based on specific metric requirements
    }

    showToast(message, type = 'info') {
        // Create toast notification
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-bg-${type === 'error' ? 'danger' : type} border-0`;
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;

        const container = document.getElementById('toastContainer') || this.createToastContainer();
        container.appendChild(toast);

        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();

        // Remove toast after it's hidden
        toast.addEventListener('hidden.bs.toast', () => {
            toast.remove();
        });
    }

    createToastContainer() {
        const container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container position-fixed top-0 end-0 p-3';
        document.body.appendChild(container);
        return container;
    }

    showError(message) {
        this.showToast(message, 'error');
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.smartCityPortal = new SmartCityPortal();
});

// Utility functions
const Utils = {
    formatNumber: (num) => {
        if (num >= 1000000) {
            return (num / 1000000).toFixed(1) + 'M';
        }
        if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'K';
        }
        return num.toString();
    },

    formatTime: (dateString) => {
        const date = new Date(dateString);
        return date.toLocaleTimeString();
    },

    formatDate: (dateString) => {
        const date = new Date(dateString);
        return date.toLocaleDateString();
    },

    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
};

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { SmartCityPortal, Utils };
}
