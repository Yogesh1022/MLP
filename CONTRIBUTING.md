# Contributing to ML Pipeline Project

Thank you for considering contributing to this project! Here are some guidelines to help you get started.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/ml-pipeline-project.git`
3. Create a new branch for your feature: `git checkout -b feature/your-feature-name`

## Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the package in editable mode with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Code Style

This project follows PEP 8 guidelines. Please ensure your code adheres to these standards:

- Use `black` for code formatting:
  ```bash
  black src/ tests/
  ```

- Use `isort` for import sorting:
  ```bash
  isort src/ tests/
  ```

- Use `flake8` for linting:
  ```bash
  flake8 src/ tests/
  ```

## Testing

All new features should include appropriate tests:

1. Write tests in the `tests/` directory
2. Use pytest for testing:
   ```bash
   pytest tests/
   ```

3. Ensure code coverage is maintained:
   ```bash
   pytest --cov=src/mlp --cov-report=html
   ```

## Documentation

- Add docstrings to all functions, classes, and modules
- Follow NumPy docstring style
- Update README.md if adding new features

## Pull Request Process

1. Ensure all tests pass
2. Update documentation as needed
3. Add a clear description of your changes
4. Reference any related issues
5. Request review from maintainers

## Code Review

All submissions require review. We use GitHub pull requests for this purpose.

## Commit Messages

Write clear, descriptive commit messages:
- Use present tense ("Add feature" not "Added feature")
- First line should be 50 characters or less
- Reference issues when applicable

## Questions?

Feel free to open an issue for any questions or concerns.

Thank you for contributing!
