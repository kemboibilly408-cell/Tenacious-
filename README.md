# Python Data Science Project

A comprehensive Python-based data science project with machine learning, data analysis, and visualization capabilities.

## Features

- 📊 Data Analysis & Visualization
- 🤖 Machine Learning with scikit-learn and XGBoost
- 🧠 Deep Learning support (TensorFlow, PyTorch)
- 📓 Jupyter Notebook integration
- 🧪 Comprehensive testing with pytest
- 🐳 Docker support
- ✨ Code quality tools (Black, Flake8, isort, Pylint)
- 📦 Pre-commit hooks for clean commits

## Personal Mission

> I built myself on consistency, self-confidence, self discipline, hardworking to achieve my goals

This repository represents my journey of personal growth through data science and machine learning.

## Project Structure

```
├── data/                    # Data files (raw, processed, external)
│   ├── raw/                # Original data
│   ├── processed/          # Cleaned/transformed data
│   └── external/           # External datasets
├── notebooks/              # Jupyter notebooks for exploration
├── src/                    # Source code
│   ├── data/              # Data loading and processing
│   ├── features/          # Feature engineering
│   ├── models/            # Model training and inference
│   └── utils/             # Utility functions
├── tests/                 # Unit tests
├── outputs/               # Results, models, visualizations
├── docker/                # Docker configuration
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup
├── pytest.ini            # Pytest configuration
├── .flake8               # Flake8 configuration
├── .pre-commit-config.yaml # Pre-commit hooks
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. Clone the repository
```bash
git clone https://github.com/kemboibilly408-cell/Tenacious-.git
cd Tenacious-
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

### Usage

#### Running Jupyter Notebooks
```bash
jupyter lab
```

#### Training Models
```bash
python src/models/train.py
```

#### Running Tests
```bash
pytest tests/
pytest tests/ --cov=src  # With coverage
```

#### Code Quality Checks
```bash
black src/
flake8 src/
isort src/
pylint src/
```

### Docker

Build and run with Docker:
```bash
docker build -f docker/Dockerfile -t data-science-project .
docker run -it data-science-project
```

Or with Docker Compose:
```bash
docker-compose -f docker/docker-compose.yml up
```

Access Jupyter at: `http://localhost:8888`

## Key Technologies

- **Data Processing**: Pandas, NumPy
- **Machine Learning**: scikit-learn, XGBoost
- **Deep Learning**: TensorFlow, PyTorch
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Testing**: pytest, pytest-cov
- **Code Quality**: Black, Flake8, isort, Pylint

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Progress

Track project goals and milestones in [docs/GOALS.md](docs/GOALS.md).

---

**Remember**: Consistency beats perfection. Keep showing up! 💪
