import os
import sys
import platform

# Define colors and styles
colors = {
    'folder': '\033[1;32m',    # Bold Green for folders
    'js': '\033[33m',          # Yellow for JavaScript files
    'jsx': '\033[34m',         # Blue for JSX files
    'png': '\033[35m',         # Magenta for PNG files
    'ts': '\033[36m',          # Cyan for TypeScript files
    'md': '\033[31m',          # Red for README.md
    'json': '\033[96m',        # Light Cyan for JSON files
    'cjs': '\033[38;5;208m',   # Orange for CJS files
    'css': '\033[38;5;208m',   # Orange for CSS files
    'svg': '\033[38;5;51m',    # Light Blue for SVG files
    'html': '\033[38;5;75m',   # Light Green for HTML files
    'default': '\033[0m'       # Reset color
}

def colorize_filename(filename):
    if filename == 'README.md':
        color = colors['md']
    elif filename.endswith('.js'):
        color = colors['js']
    elif filename.endswith('.jsx'):
        color = colors['jsx']
    elif filename.endswith('.png'):
        color = colors['png']
    elif filename.endswith('.ts'):
        color = colors['ts']
    elif filename.endswith('.json'):
        color = colors['json']
    elif filename.endswith('.cjs'):
        color = colors['cjs']
    elif filename.endswith('.css'):
        color = colors['css']
    elif filename.endswith('.svg'):
        color = colors['svg']
    elif filename.endswith('.html'):
        color = colors['html']
    else:
        color = colors['default']
    return f"{color}{filename}{colors['default']}"

def clear_terminal():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')  # Windows
    elif system == 'Linux' or 'ANDROID_ROOT' in os.environ:
        os.system('clear')  # Linux and Termux
    else:
        print("Unsupported OS")

def print_tree(startpath, prefix=''):
    try:
        entries = os.scandir(startpath)
    except PermissionError:
        return

    for entry in entries:
        if entry.is_dir():
            if entry.name not in ('.git', 'node_modules'):
                print(f"{prefix}{colors['folder']}{entry.name}/\033[0m")
                print_tree(entry.path, prefix + "│   ")
        else:
            if entry.name != 'Makefile':
                print(f"{prefix}{colorize_filename(entry.name)}")

if __name__ == "__main__":
    clear_terminal()  # Clear terminal before printing tree
    startpath = '.'
    if len(sys.argv) > 1:
        startpath = sys.argv[1]
    print_tree(startpath)

