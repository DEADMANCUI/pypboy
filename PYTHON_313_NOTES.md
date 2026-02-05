# Python 3.13.5 Compatibility Notes

This project has been updated to fully support Python 3.13.5 and newer versions.

## Key Changes Made for Python 3.13.5 Support

### 1. Deprecated Module Replacements
- ✅ `optparse` → `argparse` (Python 3.2+)
- ✅ `imp` → `importlib.util` (Python 3.4+)
- ✅ Removed `__future__` imports (Python 3+ behavior by default)

### 2. Dependencies Updated
All dependencies have been updated to versions that support Python 3.13:
- numpy: 2.2.1 (supports Python 3.9-3.13)
- pillow: 11.0.0 (supports Python 3.9-3.13)
- pygame: 2.6.0+ (supports Python 3.6+)
- cairocffi: 1.7.1+ (supports Python 3.6+)

### 3. Package Configuration
- Updated `setup.py` to specify `python_requires='>=3.9'`
- Added Python 3.13 to classifiers in `setup.py`

### 4. Flexible Version Constraints
- Changed `requirements.txt` from pinned versions (`==`) to flexible constraints (`>=`)
- This allows pip to install compatible newer versions while maintaining stability

## Installation for Python 3.13.5

```bash
# Ensure you have Python 3.13.5 installed
python --version  # Should show Python 3.13.5

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Known Issues & Workarounds

### pygame on Raspberry Pi
If you encounter pygame installation issues on ARM devices:
```bash
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libfreetype6-dev
pip install pygame --force-reinstall
```

### Native Extensions
Python 3.13 requires compilation of C extensions. Ensure you have build tools:
```bash
sudo apt-get install python3-dev build-essential
```

## Testing Compatibility

To verify everything is working correctly with Python 3.13.5:

```bash
# Test imports
python -c "import pygame; import numpy; import PIL; print('All imports successful')"

# Run application in debug mode (if available)
python main.py --help
```

## Additional Resources

- Python 3.13 Release Notes: https://docs.python.org/3/whatsnew/3.13.html
- pygame Documentation: https://www.pygame.org/docs/
- numpy Documentation: https://numpy.org/doc/

---

Last Updated: February 2026
Tested with: Python 3.13.5 on Raspberry Pi
