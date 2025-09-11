from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os, platform, math

# ======================
# --- CUSTOMIZABLE THEME FLYER GENERATOR ---
# ======================

# ========== CUSTOMIZE YOUR THEME HERE ==========

# COMPANY INFORMATION
COMPANY_NAME = "Nestive Tech-Craft Studio"
TAGLINE = ["Transform Your", "Business", "Vision Into Reality"]  # Change middle word for accent color
SUBTITLE = "Premium Professional Solutions"

# THEME SELECTOR - Change this to switch themes
CURRENT_THEME = "tech"  # Options: "tech", "medical", "fitness", "restaurant", "beauty", "education", "creative", "custom"
# CURRENT_THEME = "medical" 
# CURRENT_THEME = "fitness" 
# CURRENT_THEME = "restaurant" 
# CURRENT_THEME = "beauty" 
# CURRENT_THEME = "education" 
# CURRENT_THEME = "creative"
# CURRENT_THEME = "custom"
 
# THEME CONFIGURATIONS
THEMES = {
    "tech": {
        'name': 'Technology',
        'bg_start': (230, 230, 250),          # Lavender
        'bg_end': (123, 104, 238),            # Medium slate blue
        'primary_text': (25, 25, 112),        # Midnight blue
        'accent_text': (220, 20, 60),         # Crimson
        'button_bg': (72, 61, 139),           # Dark slate blue
        'button_text': (255, 255, 255),
        'services': [
            ("web", "Custom Website Development"),
            ("code", "Software Solutions"), 
            ("mobile", "Mobile-First Design"),
            ("shield", "Enterprise Security"),
            ("star", "Professional Branding"),
            # ("star", "Freelancer company"),
            ("star", "24/7 Support Available"),
        ]
    },
    
    "medical": {
        'name': 'Healthcare',
        'bg_start': (240, 248, 255),          # Alice blue
        'bg_end': (176, 224, 230),            # Powder blue
        'primary_text': (25, 25, 112),        # Midnight blue
        'accent_text': (220, 20, 60),         # Crimson
        'button_bg': (70, 130, 180),          # Steel blue
        'button_text': (255, 255, 255),
        'services': [
            ("shield", "Professional Healthcare"),
            ("star", "Licensed Practitioners"), 
            ("web", "Modern Medical Equipment"),
            ("mobile", "24/7 Emergency Care"),
            ("code", "Digital Health Records"),
            ("star", "Patient-Centered Care"),
        ]
    },
    
    "fitness": {
        'name': 'Fitness',
        'bg_start': (255, 69, 0),             # Red orange
        'bg_end': (255, 140, 0),              # Dark orange
        'primary_text': (139, 0, 0),          # Dark red
        'accent_text': (255, 255, 255),       # White
        'button_bg': (139, 0, 0),             # Dark red
        'button_text': (255, 255, 255),
        'services': [
            ("star", "Personal Training"),
            ("shield", "Nutrition Coaching"), 
            ("mobile", "Flexible Scheduling"),
            ("web", "Group Fitness Classes"),
            ("code", "Progress Tracking"),
            ("star", "Results Guaranteed"),
        ]
    },
    
    "restaurant": {
        'name': 'Restaurant',
        'bg_start': (255, 218, 185),          # Peach
        'bg_end': (205, 133, 63),             # Peru
        'primary_text': (101, 67, 33),        # Dark brown
        'accent_text': (178, 34, 34),         # Fire brick
        'button_bg': (178, 34, 34),           # Fire brick
        'button_text': (255, 255, 255),
        'services': [
            ("star", "Fresh Ingredients Daily"),
            ("shield", "Expert Chefs"), 
            ("mobile", "Online Ordering"),
            ("web", "Catering Services"),
            ("code", "Special Dietary Options"),
            ("star", "Exceptional Service"),
        ]
    },
    
    "beauty": {
        'name': 'Beauty & Wellness',
        'bg_start': (255, 192, 203),          # Pink
        'bg_end': (221, 160, 221),            # Plum
        'primary_text': (72, 61, 139),        # Dark slate blue
        'accent_text': (199, 21, 133),        # Medium violet red
        'button_bg': (199, 21, 133),          # Medium violet red
        'button_text': (255, 255, 255),
        'services': [
            ("star", "Professional Makeup"),
            ("shield", "Skincare Treatments"), 
            ("mobile", "Flexible Appointments"),
            ("web", "Bridal Packages"),
            ("code", "Premium Products"),
            ("star", "Expert Stylists"),
        ]
    },
    
    "education": {
        'name': 'Education',
        'bg_start': (230, 230, 250),          # Lavender
        'bg_end': (123, 104, 238),            # Medium slate blue
        'primary_text': (25, 25, 112),        # Midnight blue
        'accent_text': (220, 20, 60),         # Crimson
        'button_bg': (72, 61, 139),           # Dark slate blue
        'button_text': (255, 255, 255),
        'services': [
            ("star", "Expert Instructors"),
            ("shield", "Certified Programs"), 
            ("mobile", "Flexible Learning"),
            ("web", "Online Resources"),
            ("code", "Career Support"),
            ("star", "Proven Results"),
        ]
    },
    
    "creative": {
        'name': 'Creative Design',
        'bg_start': (255, 20, 147),           # Deep pink
        'bg_end': (138, 43, 226),             # Blue violet
        'primary_text': (75, 0, 130),         # Indigo
        'accent_text': (255, 215, 0),         # Gold
        'button_bg': (255, 215, 0),           # Gold
        'button_text': (75, 0, 130),          # Indigo
        'services': [
            ("logo", "Graphic Design"),
            ("web", "Brand Identity"), 
            ("star", "Creative Concepts"),
            ("mobile", "Digital Marketing"),
            ("code", "Web Design"),
            ("shield", "Professional Quality"),
        ]
    },
    
    # CUSTOM THEME - Edit these values for your own theme
    "custom": {
        'name': 'Custom',
        'bg_start': (173, 216, 230),          # Light blue
        'bg_end': (70, 130, 180),             # Steel blue
        'primary_text': (25, 25, 112),        # Midnight blue
        'accent_text': (220, 20, 60),         # Crimson
        'button_bg': (220, 20, 60),           # Crimson
        'button_text': (255, 255, 255),
        'services': [
            ("star", "Custom Service 1"),
            ("shield", "Custom Service 2"), 
            ("mobile", "Custom Service 3"),
            ("web", "Custom Service 4"),
            ("code", "Custom Service 5"),
            ("logo", "Custom Service 6"),
        ]
    }
}

# Validate theme selection
if CURRENT_THEME not in THEMES:
    print(f"ERROR: Invalid theme '{CURRENT_THEME}'. Using 'tech' as fallback.")
    CURRENT_THEME = "tech"

# Apply selected theme
current_theme_config = THEMES[CURRENT_THEME]
COLORS = {
    'bg_start': current_theme_config['bg_start'],
    'bg_end': current_theme_config['bg_end'],
    'primary_text': current_theme_config['primary_text'],
    'accent_text': current_theme_config['accent_text'],
    'button_bg': current_theme_config['button_bg'],
    'button_text': current_theme_config['button_text'],
    'white': (255, 255, 255),
    'btn_shadow': tuple(max(0, c-60) for c in current_theme_config['button_bg']),
    'icon_color': current_theme_config['primary_text'],
}

SERVICES = current_theme_config['services']

# ========== END CUSTOMIZATION SECTION ==========

def get_best_font(size, weight='regular'):
    """Get the best available font with proper error handling"""
    try:
        system = platform.system()
        
        if system == "Windows":
            fonts = {
                'regular': ['arial.ttf', 'calibri.ttf', 'segoeui.ttf', 'tahoma.ttf'],
                'bold': ['arialbd.ttf', 'calibrib.ttf', 'segoeuib.ttf', 'tahomabd.ttf'],
                'black': ['arialbd.ttf', 'impact.ttf', 'calibrib.ttf']
            }
        elif system == "Darwin":  # macOS
            fonts = {
                'regular': ['Arial.ttf', 'Helvetica.ttc', 'AppleSystemUIFont.ttc'],
                'bold': ['Arial Bold.ttf', 'Helvetica-Bold.ttc', 'AppleSystemUIFont.ttc'],
                'black': ['Arial Black.ttf', 'Helvetica-Bold.ttc', 'AppleSystemUIFont.ttc']
            }
        else:  # Linux
            fonts = {
                'regular': ['DejaVuSans.ttf', 'LiberationSans-Regular.ttf', 'Ubuntu-R.ttf'],
                'bold': ['DejaVuSans-Bold.ttf', 'LiberationSans-Bold.ttf', 'Ubuntu-B.ttf'],
                'black': ['DejaVuSans-Bold.ttf', 'LiberationSans-Bold.ttf']
            }
        
        # Try to load fonts in order of preference
        for font_name in fonts.get(weight, fonts['regular']):
            try:
                font = ImageFont.truetype(font_name, size)
                return font
            except (OSError, IOError):
                continue
        
        # If no system fonts work, try default font with size
        try:
            return ImageFont.load_default()
        except:
            # Last resort - create a dummy font
            print(f"Warning: Using fallback font for size {size}")
            return ImageFont.load_default()
            
    except Exception as e:
        print(f"Font loading error: {e}")
        return ImageFont.load_default()

def get_text_size(text, font):
    """Get text dimensions with compatibility for different PIL versions"""
    try:
        # Try modern PIL method first
        if hasattr(font, 'getbbox'):
            bbox = font.getbbox(text)
            return bbox[2] - bbox[0], bbox[3] - bbox[1]
        else:
            # Fallback for older PIL versions
            return font.getsize(text)
    except Exception as e:
        # Emergency fallback calculation
        print(f"Text size calculation error: {e}")
        char_width = getattr(font, 'size', 12) * 0.6  # Approximate character width
        char_height = getattr(font, 'size', 12)
        return int(len(text) * char_width), int(char_height)

def load_user_logo(logo_path, target_size):
    """Load and resize user's logo file and place it in a round white container"""
    if not logo_path:
        print("No logo path provided")
        return None
        
    try:
        # Check if file exists
        if not os.path.exists(logo_path):
            print(f"Logo file not found: {logo_path}")
            return None
            
        # Check file size (avoid loading huge files)
        file_size = os.path.getsize(logo_path) / (1024 * 1024)  # MB
        if file_size > 50:  # 50MB limit
            print(f"Logo file too large: {file_size:.1f}MB")
            return None
        
        # Load the user's logo
        logo = Image.open(logo_path)
        
        # Convert to RGBA if not already
        if logo.mode != 'RGBA':
            logo = logo.convert('RGBA')
        
        # Validate logo dimensions
        original_width, original_height = logo.size
        if original_width == 0 or original_height == 0:
            print("Invalid logo dimensions")
            return None
            
        # Calculate new dimensions for the logo (smaller than container)
        aspect_ratio = original_width / original_height
        
        # Logo should be 70% of the container size to leave padding
        logo_size = int(target_size * 0.7)
        
        if aspect_ratio > 1:  # Wide logo
            new_width = logo_size
            new_height = int(logo_size / aspect_ratio)
        else:  # Tall or square logo
            new_height = logo_size
            new_width = int(logo_size * aspect_ratio)
        
        # Ensure minimum size
        new_width = max(new_width, 20)
        new_height = max(new_height, 20)
        
        # Resize the logo
        logo = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Create round white container
        container = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(container)
        
        # Draw white circle with subtle shadow
        shadow_offset = 8
        shadow_color = (0, 0, 0, 30)  # Semi-transparent black
        
        # Draw shadow circle
        draw.ellipse([shadow_offset, shadow_offset, 
                     target_size + shadow_offset - 8, target_size + shadow_offset - 8], 
                    fill=shadow_color)
        
        # Draw main white circle
        draw.ellipse([0, 0, target_size, target_size], 
                    fill=(255, 255, 255, 255), 
                    outline=(230, 230, 230, 255), width=2)
        
        # Center the logo in the container
        logo_x = (target_size - logo.width) // 2
        logo_y = (target_size - logo.height) // 2
        
        # Paste the logo onto the container
        container.paste(logo, (logo_x, logo_y), logo)
        
        print(f"Logo loaded successfully: {logo_path}")
        return container
        
    except Exception as e:
        print(f"Error loading logo from {logo_path}: {e}")
        return None

def create_gradient_background(width, height):
    """Create a gradient background based on current theme"""
    try:
        bg = Image.new("RGB", (width, height), COLORS['bg_start'])
        
        # Simple vertical gradient with error handling
        for y in range(height):
            try:
                ratio = y / height if height > 0 else 0
                # Smooth gradient from start to end color
                r = int(COLORS['bg_start'][0] * (1-ratio) + COLORS['bg_end'][0] * ratio)
                g = int(COLORS['bg_start'][1] * (1-ratio) + COLORS['bg_end'][1] * ratio)
                b = int(COLORS['bg_start'][2] * (1-ratio) + COLORS['bg_end'][2] * ratio)
                
                # Ensure color values are within valid range
                r = max(0, min(255, r))
                g = max(0, min(255, g))
                b = max(0, min(255, b))
                
                # Draw line instead of individual pixels for efficiency
                for x in range(width):
                    bg.putpixel((x, y), (r, g, b))
            except Exception as e:
                # If pixel operation fails, continue with next line
                continue
        
        return bg
    except Exception as e:
        print(f"Error creating gradient background: {e}")
        # Return solid color background as fallback
        return Image.new("RGB", (width, height), COLORS['bg_start'])

def draw_centered_text(draw, text, font, x, y, width, color):
    """Draw centered text with error handling"""
    try:
        text_width, text_height = get_text_size(text, font)
        text_x = x + (width - text_width) // 2
        draw.text((text_x, y), text, font=font, fill=color)
        return text_height
    except Exception as e:
        print(f"Error drawing text '{text}': {e}")
        return 20  # Return approximate text height

def create_simple_button(width, height, text, font):
    """Create a simple, clean button"""
    try:
        button = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(button)
        
        # Simple rounded rectangle
        radius = min(height//2, 20)  # Limit radius
        draw.rounded_rectangle([0, 0, width, height], radius=radius, fill=COLORS['button_bg'])
        
        return button
    except Exception as e:
        print(f"Error creating button: {e}")
        # Return simple rectangle fallback
        button = Image.new("RGBA", (width, height), COLORS['button_bg'])
        return button

def draw_simple_icon(draw, x, y, size, icon_type, color):
    """Draw simple, clean icons with error handling"""
    try:
        center_x, center_y = x + size//2, y + size//2
        line_width = max(2, size//12)  # Scale line width with icon size
        
        # Ensure coordinates are within reasonable bounds
        if x < 0 or y < 0 or size <= 0:
            return
        
        if icon_type == "web":
            # Simple globe
            draw.ellipse([x+5, y+5, x+size-5, y+size-5], outline=color, width=line_width)
            draw.line([center_x, y+5, center_x, y+size-5], fill=color, width=max(1, line_width-1))
            draw.line([x+5, center_y, x+size-5, center_y], fill=color, width=max(1, line_width-1))
        
        elif icon_type == "code":
            # Simple brackets
            draw.line([(x+8, center_y), (x+15, y+8), (x+15, y+size-8)], fill=color, width=line_width)
            draw.line([(x+size-8, center_y), (x+size-15, y+8), (x+size-15, y+size-8)], fill=color, width=line_width)
        
        elif icon_type == "mobile":
            # Simple phone
            draw.rounded_rectangle([x+8, y+3, x+size-8, y+size-3], radius=6, outline=color, width=line_width)
            draw.rounded_rectangle([x+12, y+8, x+size-12, y+size-12], radius=3, outline=color, width=max(1, line_width-1))
        
        elif icon_type == "shield":
            # Simple shield
            points = [center_x, y+5, x+10, y+12, x+10, y+size-8, center_x, y+size-3, x+size-10, y+size-8, x+size-10, y+12]
            draw.polygon(points, outline=color, width=line_width)
        
        elif icon_type == "star":
            # Simple star/quality symbol
            draw.ellipse([x+8, y+8, x+size-8, y+size-8], outline=color, width=line_width)
            draw.line([center_x-6, center_y, center_x+6, center_y], fill=color, width=line_width)
            draw.line([center_x, center_y-6, center_x, center_y+6], fill=color, width=line_width)
        
        elif icon_type == "logo":
            # Simple design/logo icon - palette and brush
            draw.ellipse([x+5, y+8, x+size-12, y+size-8], outline=color, width=max(1, line_width-1))
            draw.line([x+size-15, y+5, x+size-5, y+15], fill=color, width=max(1, line_width-1))
            # Color dots on palette
            dot_size = max(1, size//20)
            dots = [(x+12, y+15), (x+18, y+20), (x+15, y+25)]
            for dot_x, dot_y in dots:
                draw.ellipse([dot_x-dot_size, dot_y-dot_size, dot_x+dot_size, dot_y+dot_size], fill=color)
                
    except Exception as e:
        print(f"Error drawing icon '{icon_type}': {e}")

def generate_themed_flyer(width, height, filename, mode="poster", logo_path=None):
    """Generate themed flyer with user's logo in round white container"""
    try:
        print(f"Creating {current_theme_config['name'].upper()} themed {mode.upper()} ({width}x{height})...")
        
        # Validate dimensions
        if width <= 0 or height <= 0:
            print(f"Invalid dimensions: {width}x{height}")
            return False
            
        if width > 5000 or height > 5000:
            print(f"Dimensions too large: {width}x{height}. Consider smaller sizes.")
            return False
        
        # Create themed background
        bg = create_gradient_background(width, height)
        draw = ImageDraw.Draw(bg)
        
        # Sizing
        size_mult = 1.2 if mode == "story" else (0.9 if mode == "social" else 1.0)
        
        # Fonts with error handling
        try:
            hero_font = get_best_font(int(80 * size_mult), 'bold')
            accent_font = get_best_font(int(80 * size_mult), 'bold')
            subtitle_font = get_best_font(int(36 * size_mult), 'regular')
            service_font = get_best_font(int(28 * size_mult), 'regular')
            button_font = get_best_font(int(32 * size_mult), 'bold')
            footer_font = get_best_font(int(24 * size_mult), 'bold')
        except Exception as e:
            print(f"Font loading error: {e}")
            # Use default fonts as fallback
            default_font = ImageFont.load_default()
            hero_font = accent_font = subtitle_font = service_font = button_font = footer_font = default_font
        
        margin = int(40 * size_mult)
        current_y = int(30 * size_mult)
        
        # ADD USER'S LOGO IN ROUND WHITE CONTAINER
        logo_container_size = int(140 * size_mult)
        
        if logo_path:
            logo_container = load_user_logo(logo_path, logo_container_size)
            if logo_container:
                # Center the logo container
                logo_x = (width - logo_container.width) // 2
                # Paste logo container with transparency support
                bg.paste(logo_container, (logo_x, current_y), logo_container)
                current_y += logo_container.height + int(40 * size_mult)
            else:
                print("Warning: Skipping logo - failed to load")
                current_y += int(20 * size_mult)
        else:
            current_y += int(20 * size_mult)
        
        # THEMED HEADLINE
        for i, word in enumerate(TAGLINE):
            if i < len(TAGLINE):  # Ensure we don't go out of bounds
                # Highlight the middle word (usually the business type)
                if i == 1:  # Middle word gets accent color
                    text_height = draw_centered_text(draw, word, accent_font, 0, current_y, 
                                                   width, COLORS['accent_text'])
                else:
                    text_height = draw_centered_text(draw, word, hero_font, 0, current_y, 
                                                   width, COLORS['primary_text'])
                current_y += text_height + int(8 * size_mult)
        
        # Subtitle
        current_y += int(30 * size_mult)
        subtitle_lines = [SUBTITLE, f"by {COMPANY_NAME}"]
        
        for line in subtitle_lines:
            text_height = draw_centered_text(draw, line, subtitle_font, 0, current_y, 
                                           width, COLORS['primary_text'])
            current_y += text_height + int(8 * size_mult)
        
        current_y += int(50 * size_mult)
        
        # THEMED SERVICES LIST
        icon_size = int(50 * size_mult)
        
        if mode == "poster":
            # Two columns for poster
            col_width = (width - 3 * margin) // 2
            service_height = int(70 * size_mult)
            
            for i, (icon_type, service) in enumerate(SERVICES):
                if i < len(SERVICES):  # Safety check
                    col = i % 2
                    row = i // 2
                    
                    x_pos = margin + col * (col_width + margin)
                    y_pos = current_y + row * (service_height + int(15 * size_mult))
                    
                    # Simple icon
                    draw_simple_icon(draw, x_pos, y_pos + 10, icon_size, icon_type, COLORS['icon_color'])
                    
                    # Simple service text
                    text_x = x_pos + icon_size + 15
                    text_y = y_pos + (service_height - get_text_size(service, service_font)[1]) // 2
                    draw.text((text_x, text_y), service, font=service_font, fill=COLORS['primary_text'])
            
            services_height = ((len(SERVICES) + 1) // 2) * (service_height + int(15 * size_mult))
        
        else:
            # Single column for social/story
            service_height = int(60 * size_mult)
            for i, (icon_type, service) in enumerate(SERVICES):
                if i < len(SERVICES):  # Safety check
                    y_pos = current_y + i * (service_height + int(10 * size_mult))
                    
                    # Icon and text
                    draw_simple_icon(draw, margin, y_pos + 5, icon_size, icon_type, COLORS['icon_color'])
                    
                    text_x = margin + icon_size + 15
                    text_y = y_pos + (service_height - get_text_size(service, service_font)[1]) // 2
                    draw.text((text_x, text_y), service, font=service_font, fill=COLORS['primary_text'])
            
            services_height = len(SERVICES) * (service_height + int(10 * size_mult))
        
        current_y += services_height + int(50 * size_mult)
        
        # Add support text
        support_text = "Professional Service Available"
        text_height = draw_centered_text(draw, support_text, service_font, 0, current_y, 
                                       width, COLORS['primary_text'])
        current_y += text_height + int(30 * size_mult)
        
        # THEMED BUTTON
        if mode == "social":
            button_text = "Click on see more"
            button_width = int(350 * size_mult)
            button_height = int(70 * size_mult)
        else:
            button_text = "Get Free Consultation\n& Quick Project Quote"
            button_width = int(500 * size_mult)
            button_height = int(90 * size_mult)
        
        button_x = (width - button_width) // 2
        
        # Simple shadow
        shadow_offset = 5
        draw.rounded_rectangle([button_x + shadow_offset, current_y + shadow_offset, 
                               button_x + button_width + shadow_offset, 
                               current_y + button_height + shadow_offset], 
                              radius=min(button_height//2, 20), 
                              fill=COLORS['btn_shadow'])
        
        # Create and paste button
        button_img = create_simple_button(button_width, button_height, button_text, button_font)
        bg.paste(button_img, (button_x, current_y), button_img)
        
        # Button text
        if '\n' in button_text:
            lines = button_text.split('\n')
            line_height = button_height // len(lines)
            start_y = current_y + (button_height - len(lines) * line_height) // 2
            
            for i, line in enumerate(lines):
                line_y = start_y + i * line_height
                text_width, _ = get_text_size(line, button_font)
                text_x = button_x + (button_width - text_width) // 2
                draw.text((text_x, line_y), line, font=button_font, fill=COLORS['button_text'])
        else:
            text_width, text_height = get_text_size(button_text, button_font)
            text_x = button_x + (button_width - text_width) // 2
            text_y = current_y + (button_height - text_height) // 2
            draw.text((text_x, text_y), button_text, font=button_font, fill=COLORS['button_text'])
        
        current_y += button_height + int(40 * size_mult)
        
        # Footer (for poster and story)
        if mode != "social" and current_y < height - 120:
            footer_y = height - int(100 * size_mult)
            
            # Footer text
            footer_left = f"Delivering {current_theme_config['name']} Excellence\nThrough Professional Service"
            left_lines = footer_left.split('\n')
            for i, line in enumerate(left_lines):
                draw.text((margin, footer_y + i * int(25 * size_mult)), 
                         line, font=footer_font, fill=COLORS['primary_text'])
            
            footer_right = "From Consultation to Completion -\nWe've Got You Covered"
            right_lines = footer_right.split('\n')
            for i, line in enumerate(right_lines):
                text_width, _ = get_text_size(line, footer_font)
                x_pos = width - margin - text_width
                draw.text((x_pos, footer_y + i * int(25 * size_mult)), 
                         line, font=footer_font, fill=COLORS['primary_text'])
        
        # Save with better error handling
        try:
            # Ensure output directory exists
            output_dir = os.path.dirname(filename) if os.path.dirname(filename) else '.'
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # Convert to RGB if saving as JPEG or if RGBA causes issues
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
                # Convert RGBA to RGB for JPEG
                rgb_bg = Image.new("RGB", bg.size, (255, 255, 255))
                rgb_bg.paste(bg, mask=bg.split()[-1] if bg.mode == 'RGBA' else None)
                rgb_bg.save(filename, "JPEG", quality=95, optimize=True)
            else:
                bg.save(filename, "PNG", optimize=True)
                
            print(f"{current_theme_config['name'].upper()} themed {mode.upper()} SAVED: {filename}")
            return True
            
        except PermissionError:
            print(f"Permission denied: Cannot write to {filename}")
            return False
        except OSError as e:
            print(f"File system error: {e}")
            return False
        except Exception as e:
            print(f"Save error: {e}")
            return False
            
    except Exception as e:
        print(f"Fatal error generating flyer: {e}")
        import traceback
        traceback.print_exc()
        return False

def validate_logo_path(logo_path):
    """Validate logo file path and suggest alternatives"""
    if not logo_path:
        return None
        
    # Check if exact path exists
    if os.path.exists(logo_path):
        return logo_path
    
    # Try common variations
    base_name = os.path.splitext(os.path.basename(logo_path))[0]
    common_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp']
    
    for ext in common_extensions:
        test_path = base_name + ext
        if os.path.exists(test_path):
            print(f"Found logo: {test_path}")
            return test_path
    
    # Try in common directories
    common_dirs = ['.', 'images', 'assets', 'logos']
    for directory in common_dirs:
        for ext in common_extensions:
            test_path = os.path.join(directory, base_name + ext)
            if os.path.exists(test_path):
                print(f"Found logo: {test_path}")
                return test_path
    
    print(f"Logo not found: {logo_path}")
    print("Tip: Place your logo file in the same directory as this script")
    return None

def generate_all_themed_flyers():
    """Generate all themed designs with comprehensive error handling"""
    print(f"GENERATING {current_theme_config['name'].upper()} THEMED FLYERS")
    print("=" * 70)
    
    # SET YOUR LOGO PATH HERE - UPDATED WITH VALIDATION
    LOGO_PATH = "Media-removebg-preview.png"  # Your logo file
    
    # Validate logo path
    validated_logo_path = validate_logo_path(LOGO_PATH)
    
    theme_prefix = CURRENT_THEME.lower()
    designs = [
        {"width": 1200, "height": 1600, "filename": f"{theme_prefix}_poster_themed.png", "mode": "poster", "logo_path": validated_logo_path},
        {"width": 1080, "height": 1080, "filename": f"{theme_prefix}_social_themed.png", "mode": "social", "logo_path": validated_logo_path},
        {"width": 1080, "height": 1920, "filename": f"{theme_prefix}_story_themed.png", "mode": "story", "logo_path": validated_logo_path}
    ]
    
    success = 0
    failed_designs = []
    
    for design in designs:
        try:
            if generate_themed_flyer(**design):
                success += 1
            else:
                failed_designs.append(design['filename'])
        except Exception as e:
            print(f"Failed to generate {design['filename']}: {e}")
            failed_designs.append(design['filename'])
    
    print("=" * 70)
    print(f"RESULTS: {success}/3 {current_theme_config['name'].upper()} themed designs created!")
    
    if failed_designs:
        print(f"Failed designs: {', '.join(failed_designs)}")
        print("\nTroubleshooting tips:")
        print("1. Check if you have write permissions in the current directory")
        print("2. Ensure your logo file exists and is a valid image format")
        print("3. Try running as administrator if on Windows")
        print("4. Check available disk space")
    
    if success == 3:
        print(f"\n✅ ALL {current_theme_config['name'].upper()} THEME DESIGNS COMPLETED!")
        print(f"   Background: Custom gradient colors")
        print(f"   Logo: Round white container with shadow")
        print(f"   Typography: Professional and readable")
        print(f"   Services: Theme-appropriate content")
        print(f"   Colors: Coordinated theme palette")
        print(f"   Layout: Clean and professional")
    elif success > 0:
        print(f"\n⚠️ PARTIAL SUCCESS: {success} design(s) completed")
    else:
        print(f"\n❌ NO DESIGNS COMPLETED - Check error messages above")

def print_theme_info():
    """Print information about available themes"""
    print("AVAILABLE THEMES:")
    print("=" * 50)
    for theme_key, theme_info in THEMES.items():
        status = "✅ ACTIVE" if theme_key == CURRENT_THEME else ""
        print(f"{theme_key.upper()}: {theme_info['name']} {status}")
    print("=" * 50)
    print(f"CURRENT THEME: {CURRENT_THEME.upper()} ({current_theme_config['name']})")
    print(f"TO CHANGE THEME: Set CURRENT_THEME = 'theme_name' at the top")

def run_system_checks():
    """Run comprehensive system checks before generating flyers"""
    print("RUNNING SYSTEM CHECKS...")
    print("-" * 30)
    
    issues_found = []
    
    # Check PIL installation
    try:
        from PIL import Image, ImageDraw, ImageFont
        print("✅ PIL/Pillow installed correctly")
    except ImportError as e:
        print(f"❌ PIL/Pillow import error: {e}")
        issues_found.append("Install Pillow: pip install Pillow")
    
    # Check write permissions
    try:
        test_file = "test_write_permission.tmp"
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
        print("✅ Write permissions OK")
    except Exception as e:
        print(f"❌ Write permission error: {e}")
        issues_found.append("Check directory write permissions")
    
    # Check available fonts
    try:
        font = get_best_font(20)
        print("✅ Font system working")
    except Exception as e:
        print(f"⚠️ Font system warning: {e}")
        issues_found.append("Font rendering may use defaults")
    
    # Check theme configuration
    if CURRENT_THEME in THEMES:
        print(f"✅ Theme '{CURRENT_THEME}' loaded successfully")
    else:
        print(f"❌ Invalid theme: {CURRENT_THEME}")
        issues_found.append(f"Use valid theme name")
    
    # Check logo file
    logo_path = "Media-removebg-preview.png"  # Default logo path
    validated_path = validate_logo_path(logo_path)
    if validated_path:
        print(f"✅ Logo file found: {validated_path}")
    else:
        print(f"⚠️ Logo file not found: {logo_path}")
        issues_found.append("Place logo file in script directory or update LOGO_PATH")
    
    print("-" * 30)
    if issues_found:
        print("⚠️ ISSUES TO RESOLVE:")
        for issue in issues_found:
            print(f"   • {issue}")
        return False
    else:
        print("✅ ALL CHECKS PASSED - Ready to generate flyers!")
        return True

if __name__ == "__main__":
    print(f"{current_theme_config['name'].upper()} THEMED FLYER GENERATOR")
    print("=" * 80)
    print(f"Company: {COMPANY_NAME}")
    print(f"Theme: {current_theme_config['name']}")
    print("=" * 80)
    
    # Run system checks first
    if run_system_checks():
        print("\n")
        print_theme_info()
        print("\n")
        generate_all_themed_flyers()
        print(f"\nREADY FOR PROFESSIONAL BUSINESS USE WITH {current_theme_config['name'].upper()} THEME!")
    else:
        print("\n❌ Please resolve the issues above before generating flyers.")
        print("You can still try running generate_all_themed_flyers() if you want to proceed anyway.")