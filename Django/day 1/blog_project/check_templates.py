# check_templates.py
import os
import sys
from pathlib import Path

# Add the project to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Now we can import Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

try:
    import django
    django.setup()
    
    from django.conf import settings
    from django.template.loader import get_template
    
    print("=" * 60)
    print("DIAGNOSTIC CHECK - TEMPLATE CONFIGURATION")
    print("=" * 60)
    
    # Check 1: Base directory
    print(f"\n1. BASE_DIR: {settings.BASE_DIR}")
    print(f"   Project root exists: {settings.BASE_DIR.exists()}")
    
    # Check 2: Template directories
    print(f"\n2. TEMPLATE DIRS: {settings.TEMPLATES[0]['DIRS']}")
    
    # Check 3: Test each template directory
    for i, template_dir in enumerate(settings.TEMPLATES[0]['DIRS']):
        print(f"   Template dir {i}: {template_dir}")
        print(f"   Exists: {template_dir.exists()}")
        
        # Check for test.html
        test_path = template_dir / 'blog' / 'test.html'
        print(f"   test.html path: {test_path}")
        print(f"   test.html exists: {test_path.exists()}")
    
    # Check 4: Try to load template
    print(f"\n3. Testing template loading...")
    try:
        template = get_template('blog/test.html')
        print(f"   ✓ SUCCESS: Template loaded from: {template.origin}")
    except Exception as e:
        print(f"   ✗ ERROR loading template: {e}")
        print(f"   Full error details:")
        import traceback
        traceback.print_exc()
    
    # Check 5: List files in templates directory
    print(f"\n4. Files in templates directory:")
    templates_dir = settings.BASE_DIR / 'templates'
    if templates_dir.exists():
        for root, dirs, files in os.walk(templates_dir):
            level = root.replace(str(templates_dir), '').count(os.sep)
            indent = ' ' * 2 * level
            print(f'{indent}{os.path.basename(root)}/')
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                print(f'{subindent}{file}')
    else:
        print(f"   ✗ templates directory doesn't exist at {templates_dir}")
    
    print("\n" + "=" * 60)
    print("END OF DIAGNOSTIC")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ MAJOR ERROR: {e}")
    import traceback
    traceback.print_exc()