## 🎨 User Interface

PrintOptimazer features a polished, dark-mode dashboard with a consistent color palette:

| Element | Color Code |
|:--------|:-----------|
| Background | `#1E1E1E` |
| Primary Text | `#F5F5F5` |
| Secondary Text | `#A0A0A0` |
| Highlights & CTAs | `#E63946` |

The interface includes:
- Collapsible sidebar with icon labels for each module
- Persistent light/dark mode toggle in the header
- Responsive grid layout adapting to different screen sizes
- Smooth hover states and transitions for interactive elements
- Toast notifications providing feedback for user actions# PrintOptimazer

<div align="center">

![PrintOptimazer Logo](assets/favicon.ico)

**3D Printing Business Management & Marketplace Integration Platform**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Built with Reflex](https://img.shields.io/badge/built%20with-Reflex-blue.svg)](https://reflex.dev)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://printoptimazer.readthedocs.io)

</div>

---

## 📋 Overview

PrintOptimazer is a comprehensive 3D printing business management platform that unifies data from multiple marketplace channels (Thingiverse, MyMiniFactory, Cults3D, Patreon) while providing powerful tools for project tracking, cost management, and business analytics. Designed with a polished dark-mode interface, it centralizes all aspects of running a 3D printing business from marketplace performance to inventory management.

## ✨ Key Features

| Category | Features |
|:---------|:---------|
| **Marketplace Integration** | • Thingiverse, MyMiniFactory, Cults3D, and Patreon integration<br>• Unified views, downloads, and revenue tracking<br>• Cross-platform performance analytics<br>• Multiple payment method tracking (PayPal, credit cards, crypto) |
| **Project Management** | • Project registration and status tracking<br>• Cross-platform publication scheduling<br>• Client management<br>• Budget and milestone tracking |
| **Financial Tools** | • Real-time cost control and analysis<br>• Revenue tracking by marketplace<br>• Profit margin calculation<br>• Unit cost management for materials and labor |
| **Inventory & Materials** | • Material stock tracking<br>• Order placement and management<br>• Reorder threshold alerts<br>• Supplier management |
| **AI Content Creation** | • SEO-optimized title generation<br>• Platform-specific description writing<br>• Tag suggestion and optimization<br>• Content performance tracking |
| **Quotation System** | • Custom client quotation creation<br>• Configurable markup settings<br>• Quote tracking and management<br>• Conversion rate analytics |
| **File Management** | • STL/3MF file upload tracking<br>• Cross-platform synchronization status<br>• Retry controls for failed uploads<br>• File version management |
| **Analytics & Reporting** | • Interactive trend visualization<br>• Platform comparison tools<br>• PDF report generation<br>• Custom date range filtering |

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Reflex framework
- Modern web browser (Chrome, Firefox, Safari, or Edge recommended)

### Installation

#### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/PrintOptimazer.git
cd PrintOptimazer
```

#### 2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

#### 4. Initialize the Reflex application:
```bash
reflex init
```

#### 5. Configure environment variables (if needed):
```bash
# Create a .env file in the project root directory
# Add any required environment variables
```

## 🏗️ Project Structure

```
PrintOptimazer/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── rxconfig.py                  # Reflex configuration
├── assets/
│   └── favicon.ico              # Website favicon
│
├── blocks/                      # Core application blocks
│   └── __init__.py
│
├── printoptimizer_dashboard/    # Main dashboard module
│   ├── __init__.py
│   ├── printoptimizer_dashboard.py  # Main application
│   │
│   ├── components/              # UI components
│   │   ├── __init__.py
│   │   ├── ai_metadata_widget.py     # AI metadata processing widget
│   │   ├── cost_control_panel.py     # Cost control panel
│   │   ├── header_bar.py             # Header navigation bar
│   │   ├── interactive_calendar.py   # Interactive scheduling calendar
│   │   ├── inventory_dashboard.py    # Inventory management dashboard
│   │   ├── kpi_card.py               # KPI indicator cards
│   │   ├── mail_inbox.py             # Integrated mail inbox
│   │   ├── marketplace_integrations.py  # Marketplace connector widgets
│   │   ├── material_ordering.py      # Material ordering system
│   │   ├── pdf_export_module.py      # PDF export functionality
│   │   ├── project_registration.py   # Project registration forms
│   │   ├── quotation_area.py         # Quotation management
│   │   ├── sidebar.py                # Navigation sidebar
│   │   ├── summary_panel.py          # Dashboard summary panel
│   │   ├── trends_chart.py           # Analytics trend charts
│   │   └── upload_sync_status.py     # File synchronization status
│   │
│   └── states/                  # Application state management
│       ├── __init__.py
│       └── print_optimizer_state.py
│
└── uploaded_files/              # Directory for uploaded files
```

## 🖥️ Running the Application

```bash
# Start the Reflex development server
reflex run

# Or use the direct Python module approach
python -m printoptimizer_dashboard.printoptimizer_dashboard
```

Visit `http://localhost:3000` in your browser to access the application.

### Development Mode

For development with hot-reloading:

```bash
reflex run --dev
```

## 📊 Dashboard Components

PrintOptimazer's dashboard includes these specialized modules:

### Summary Panel
- KPI cards displaying active projects across all platforms
- Total revenue breakdowns by marketplace channel
- Average cost calculations and profit margin visualization
- At-a-glance business health indicators

### Marketplace Integrations
- Real-time feeds from Thingiverse, MyMiniFactory, Cults3D, and Patreon
- Statistics for views, downloads, and pledges
- Payment method tracking (PayPal, credit cards, cryptocurrency)
- Performance comparison between platforms

### Trends Chart
- Interactive line and bar combination charts
- Filters by platform, payment type, and date range
- Hover tooltips providing detailed data points
- Toggleable legend for customized data visualization

### AI Metadata Widget
- One-click generation of SEO-optimized titles and descriptions
- Platform-specific tag suggestions
- Automated content optimization
- Performance tracking for metadata effectiveness

### Cost Control Panel
- Collapsible table of supplies (filament, resin, power, labor)
- Real-time unit-cost calculations
- Inline price editing capabilities
- Cost trend analysis and recommendations

### Upload & Sync Status
- Card list of recent .STL/.3MF uploads and Patreon releases
- Progress bars for ongoing uploads and synchronizations
- Success/error icons with detailed status information
- Retry controls for failed synchronizations

### Project Registration Module
- Form-driven list of ongoing projects
- Fields for client, platform, expected delivery date, budget
- Status tags (planning, printing, uploaded, completed)
- Project filtering and sorting capabilities

### Administration Module
- **Inventory Dashboard**: Current stock levels with alerts
- **Material Ordering**: Purchase order management
- **Quotation Area**: Client quote generation and tracking

### Interactive Calendar
- Drag-and-drop scheduling of publications and milestones
- Color-coded events by status and platform
- Pop-up detail views for scheduled items
- Integration with project timelines

### PDF Export Module
- One-click export of consolidated reports
- Profitability and performance analytics by design or project
- Preset report templates for different business needs
- Download toast confirmations

## 🧩 Key Components

### User Interface Components

| Component | Description |
|-----------|-------------|
| **Header Bar** | Navigation controls and light/dark mode toggle |
| **Sidebar** | Collapsible navigation with icon labels for each module |
| **AI Metadata Widget** | Generates SEO-optimized titles, descriptions, and tags for 3D models across platforms |
| **Cost Control Panel** | Tracking and analysis of material, labor, and overhead costs |
| **Interactive Calendar** | Visual scheduling for marketplace uploads and project milestones |
| **Inventory Dashboard** | Material stock tracking with alerts and management tools |
| **KPI Card** | Dynamic cards displaying key performance metrics |
| **Mail Inbox** | Communication center for client and platform messages |
| **Marketplace Integrations** | Real-time data from Thingiverse, MyMiniFactory, Cults3D, and Patreon |
| **Material Ordering** | Supply procurement and vendor management system |
| **PDF Export Module** | Report generation and export functionality |
| **Project Registration** | Client project intake and management workflow |
| **Quotation Area** | Client quote creation with configurable markup rates |
| **Summary Panel** | Executive overview of cross-platform performance |
| **Trends Chart** | Interactive data visualization for marketplace metrics |
| **Upload Sync Status** | File management and cross-platform synchronization tracking |

### State Management

The application uses Reflex's state management system to handle:

- Marketplace API integration and data synchronization
- User preferences and dashboard configuration
- Real-time cost and inventory calculations
- Project status tracking and notifications

## 🔧 Configuration

PrintOptimazer can be customized through the following configuration options in `rxconfig.py`:

| Setting | Description | Default |
|---------|-------------|---------|
| `app_name` | Application name | `"printoptimizer_dashboard"` |
| `db_url` | Database connection string | `"sqlite:///PrintOptimazer.db"` |
| `env` | Environment (dev/prod) | `"dev"` |
| `frontend_port` | Frontend development port | `3000` |
| `backend_port` | Backend API port | `8000` |
| `telemetry_enabled` | Enable usage telemetry | `False` |
| `bun_path` | Path to bun binary | System default |
| `backend_host` | Backend host address | `"0.0.0.0"` |

Additional Reflex configuration options can be found in the [Reflex documentation](https://reflex.dev/docs/getting-started/configuration/).

## 📈 Roadmap

- **Q3 2025**: Mobile application optimization
- **Q4 2025**: Enhanced AI metadata processing capabilities
- **Q1 2026**: Advanced predictive analytics for print resource optimization
- **Q2 2026**: Multi-site enterprise deployment support

## 👥 Contributing

We welcome contributions from the community! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests to ensure everything works
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

Please make sure to adhere to our coding standards and include appropriate documentation.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

| Type | Channel |
|------|---------|
| **Email Support** | [support@printoptimazer.com](alvarezvillegasjoseangel@gmail.com) |

## 🙏 Acknowledgments

- Built with [Python](https://www.python.org/) and [Reflex](https://reflex.dev/)
- Thanks to all our contributors and community members
- Special thanks to the open-source projects that made this possible
