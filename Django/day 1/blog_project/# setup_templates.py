# setup_templates.py
import os
from pathlib import Path

def create_directories():
    """Create necessary directories for templates and static files"""
    # Get the project root directory (where manage.py is)
    root_dir = Path(__file__).parent
    
    print(f"Working in directory: {root_dir}")
    
    # Create directories
    directories = [
        'templates/blog',
        'static/css',
        'static/js',
        'static/images'
    ]
    
    for directory in directories:
        dir_path = root_dir / directory
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"✓ Created: {dir_path}")
        except Exception as e:
            print(f"✗ Error creating {directory}: {e}")
    
    # Create basic template files
    create_basic_templates(root_dir)
    
    print("\n" + "="*50)
    print("✓ Directory structure created successfully!")
    print("\nNow you can:")
    print("1. Add your HTML files in templates/blog/")
    print("2. Add CSS files in static/css/")
    print("3. Run: python manage.py runserver")
    print("4. Visit: http://127.0.0.1:8000/")
    print("="*50)

def create_basic_templates(root_dir):
    """Create minimal template files to get started"""
    
    # Create base.html
    base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Blog API{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">Blog API</a>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/posts/">Blog Posts</a>
                <a href="/api/posts/">API</a>
                <a href="/admin/">Admin</a>
            </div>
        </div>
    </nav>

    <main class="container">
        {% block content %}
        <!-- Page content goes here -->
        {% endblock %}
    </main>

    <footer>
        <div class="container">
            <p>© 2024 Blog API Project</p>
        </div>
    </footer>
</body>
</html>"""
    
    # Create index.html
    index_html = """{% extends 'blog/base.html' %}

{% block title %}Home - Blog API{% endblock %}

{% block content %}
<div class="hero">
    <h1>Welcome to Blog API</h1>
    <p>A full-featured blogging platform built with Django REST Framework</p>
    
    <div class="cta-buttons">
        <a href="/posts/" class="btn btn-primary">View All Posts</a>
        <a href="/api/posts/" class="btn btn-secondary">Explore API</a>
        <a href="/admin/" class="btn">Admin Panel</a>
    </div>
</div>

<div class="features">
    <div class="feature">
        <h3>📝 CRUD Operations</h3>
        <p>Create, Read, Update, and Delete blog posts</p>
    </div>
    <div class="feature">
        <h3>🔧 REST API</h3>
        <p>Complete RESTful API endpoints</p>
    </div>
    <div class="feature">
        <h3>🎨 Responsive Design</h3>
        <p>Works on all devices</p>
    </div>
</div>
{% endblock %}"""
    
    # Create style.css
    style_css = """/* Basic styles for Blog API */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f5f5f5;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

nav {
    background: #333;
    color: white;
    padding: 1rem 0;
}

nav .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    color: white;
    font-size: 1.5rem;
    font-weight: bold;
    text-decoration: none;
}

.nav-links a {
    color: white;
    text-decoration: none;
    margin-left: 1rem;
    padding: 0.5rem 1rem;
    border-radius: 4px;
}

.nav-links a:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

.hero {
    text-align: center;
    padding: 3rem 1rem;
    background: white;
    border-radius: 8px;
    margin: 2rem 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.hero h1 {
    color: #333;
    margin-bottom: 1rem;
}

.hero p {
    color: #666;
    margin-bottom: 2rem;
}

.cta-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
}

.btn {
    display: inline-block;
    padding: 0.8rem 1.5rem;
    background: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

.btn:hover {
    background: #0056b3;
}

.btn-primary {
    background: #28a745;
}

.btn-primary:hover {
    background: #1e7e34;
}

.btn-secondary {
    background: #6c757d;
}

.btn-secondary:hover {
    background: #545b62;
}

.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.feature {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.feature h3 {
    color: #333;
    margin-bottom: 1rem;
}

.feature p {
    color: #666;
}

footer {
    background: #333;
    color: white;
    text-align: center;
    padding: 2rem 0;
    margin-top: 3rem;
}

footer p {
    opacity: 0.8;
}

/* Responsive design */
@media (max-width: 768px) {
    nav .container {
        flex-direction: column;
        gap: 1rem;
    }
    
    .nav-links {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.5rem;
    }
    
    .nav-links a {
        margin: 0;
    }
    
    .cta-buttons {
        flex-direction: column;
        align-items: center;
    }
    
    .btn {
        width: 100%;
        max-width: 300px;
        text-align: center;
    }
}"""
    
    # Create post_list.html
    post_list_html = """{% extends 'blog/base.html' %}
{% load static %}

{% block title %}Blog Posts{% endblock %}

{% block content %}
<h1>Blog Posts</h1>
<div class="posts-grid">
    {% for post in posts %}
    <div class="post-card">
        <h3><a href="{% url 'post-detail' post.pk %}">{{ post.title }}</a></h3>
        <p class="post-meta">By {{ post.author.username }} | {{ post.published_date|date:"M d, Y" }}</p>
        <p>{{ post.content|truncatewords:30 }}</p>
        <a href="{% url 'post-detail' post.pk %}" class="btn">Read More</a>
    </div>
    {% empty %}
    <div class="empty-state">
        <h3>No posts yet</h3>
        <p>Be the first to create a blog post!</p>
        <a href="/admin/blog/blogpost/add/" class="btn btn-primary">Create Post</a>
    </div>
    {% endfor %}
</div>
{% endblock %}"""

    # Write files
    templates = {
        'templates/blog/base.html': base_html,
        'templates/blog/index.html': index_html,
        'templates/blog/post_list.html': post_list_html,
        'static/css/style.css': style_css
    }
    
    for filepath, content in templates.items():
        full_path = root_dir / filepath
        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Created: {full_path}")
        except Exception as e:
            print(f"✗ Error creating {filepath}: {e}")

def check_settings():
    """Check if settings.py is properly configured"""
    print("\n" + "="*50)
    print("Checking settings.py configuration...")
    
    settings_path = Path(__file__).parent / 'blog_project' / 'settings.py'
    
    if not settings_path.exists():
        print("✗ settings.py not found!")
        return
    
    try:
        with open(settings_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = [
            ("'DIRS': [BASE_DIR / 'templates']", "Template directory configured"),
            ("STATICFILES_DIRS", "Static files directory configured"),
            ("'rest_framework'", "Django REST Framework installed"),
        ]
        
        for check_str, message in checks:
            if check_str in content:
                print(f"✓ {message}")
            else:
                print(f"⚠ {message} - Please verify")
                
    except Exception as e:
        print(f"✗ Error reading settings.py: {e}")

if __name__ == "__main__":
    print("Setting up Blog API project structure...")
    print("="*50)
    
    create_directories()
    check_settings()
    
    print("\nSetup complete! Run these commands:")
    print("1. python manage.py makemigrations")
    print("2. python manage.py migrate")
    print("3. python manage.py runserver")
    print("\nThen visit: http://127.0.0.1:8000/")