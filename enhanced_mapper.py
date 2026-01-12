"""
Enhanced dungeon mapper with sophisticated SVG-based visualization.
This module provides modern, visually appealing dungeon maps while maintaining
compatibility with the original HTML table output.
"""

import html


def sanitize_for_html(value):
    """Safely convert a value to HTML-escaped string."""
    if value is None:
        return ''
    return html.escape(str(value))


def generate_enhanced_html(dungeon_data, level_num, room_stack, downlist, coord_limits):
    """
    Generate an enhanced HTML visualization with SVG-based rendering.
    
    Args:
        dungeon_data: Dictionary containing dungeon information
        level_num: The level number (0-indexed)
        room_stack: Stack containing room information
        downlist: Array of dungeon levels
        coord_limits: Tuple of (min_coords, max_coords)
    
    Returns:
        HTML string for enhanced visualization
    """
    down = level_num
    xmin, ymin, zmin = coord_limits[0]
    xmax, ymax, zmax = coord_limits[1]
    
    # Calculate dimensions
    width = xmax - xmin + 1
    height = ymax - ymin + 1
    
    # SVG cell size (larger for better detail)
    cell_size = 40
    svg_width = width * cell_size
    svg_height = height * cell_size
    
    output_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced Dungeon Map - Level {level_num + 1}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
            color: #e0e0e0;
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1600px;
            margin: 0 auto;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        }}
        
        h1 {{
            text-align: center;
            color: #ffd700;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
        }}
        
        .subtitle {{
            text-align: center;
            color: #c0c0c0;
            font-size: 1.2em;
            margin-bottom: 30px;
            font-style: italic;
        }}
        
        .map-container {{
            background: #1a1a1a;
            border: 3px solid #4a4a4a;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 30px;
            overflow: auto;
            box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.5);
        }}
        
        .map-wrapper {{
            display: inline-block;
            background: repeating-linear-gradient(
                0deg,
                transparent,
                transparent 40px,
                rgba(255, 255, 255, 0.02) 40px,
                rgba(255, 255, 255, 0.02) 41px
            ),
            repeating-linear-gradient(
                90deg,
                transparent,
                transparent 40px,
                rgba(255, 255, 255, 0.02) 40px,
                rgba(255, 255, 255, 0.02) 41px
            );
        }}
        
        .controls {{
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}
        
        .btn {{
            background: linear-gradient(135deg, #4a4a4a 0%, #2d2d2d 100%);
            color: #ffd700;
            border: 2px solid #6a6a6a;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            transition: all 0.3s ease;
            font-weight: bold;
        }}
        
        .btn:hover {{
            background: linear-gradient(135deg, #5a5a5a 0%, #3d3d3d 100%);
            border-color: #ffd700;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }}
        
        .info-panel {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .info-card {{
            background: rgba(50, 50, 50, 0.5);
            border: 2px solid #4a4a4a;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }}
        
        .info-card h3 {{
            color: #ffd700;
            margin-bottom: 15px;
            font-size: 1.3em;
            border-bottom: 2px solid #4a4a4a;
            padding-bottom: 10px;
        }}
        
        .legend {{
            background: rgba(30, 30, 30, 0.8);
            border: 2px solid #4a4a4a;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
        }}
        
        .legend h3 {{
            color: #ffd700;
            margin-bottom: 15px;
            font-size: 1.3em;
        }}
        
        .legend-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 10px;
        }}
        
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 5px;
        }}
        
        .legend-color {{
            width: 30px;
            height: 30px;
            border: 1px solid #666;
            border-radius: 3px;
            flex-shrink: 0;
        }}
        
        .room-details {{
            background: rgba(30, 30, 30, 0.8);
            border: 2px solid #4a4a4a;
            border-radius: 8px;
            padding: 20px;
            max-height: 600px;
            overflow-y: auto;
        }}
        
        .room-details h3 {{
            color: #ffd700;
            margin-bottom: 15px;
            font-size: 1.3em;
        }}
        
        .room-entry {{
            background: rgba(50, 50, 50, 0.5);
            border-left: 4px solid #6a6a6a;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
        }}
        
        .room-entry:hover {{
            border-left-color: #ffd700;
            background: rgba(60, 60, 60, 0.5);
        }}
        
        .room-title {{
            color: #ffd700;
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        
        .room-content {{
            color: #c0c0c0;
            line-height: 1.6;
        }}
        
        .room-content strong {{
            color: #fff;
        }}
        
        .treasure {{
            color: #ffd700;
        }}
        
        .monster {{
            color: #ff6b6b;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
        }}
        
        .stat-item {{
            background: rgba(70, 70, 70, 0.3);
            padding: 10px;
            border-radius: 5px;
            border-left: 3px solid #ffd700;
        }}
        
        .stat-label {{
            font-size: 0.85em;
            color: #a0a0a0;
            margin-bottom: 5px;
        }}
        
        .stat-value {{
            font-size: 1.3em;
            font-weight: bold;
            color: #ffd700;
        }}
        
        /* SVG Styles */
        .cell {{
            stroke: #333;
            stroke-width: 1;
            transition: all 0.2s ease;
        }}
        
        .cell:hover {{
            stroke: #ffd700;
            stroke-width: 3;
            filter: brightness(1.2);
        }}
        
        .cell-text {{
            font-family: 'Courier New', monospace;
            font-size: 10px;
            fill: #000;
            pointer-events: none;
            text-anchor: middle;
            dominant-baseline: middle;
            font-weight: bold;
        }}
        
        .tooltip {{
            position: absolute;
            background: rgba(0, 0, 0, 0.9);
            color: #ffd700;
            padding: 10px;
            border-radius: 5px;
            border: 2px solid #ffd700;
            font-size: 0.9em;
            pointer-events: none;
            z-index: 1000;
            display: none;
            max-width: 300px;
        }}
        
        /* Scrollbar styling */
        ::-webkit-scrollbar {{
            width: 12px;
            height: 12px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: #1a1a1a;
            border-radius: 6px;
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: #4a4a4a;
            border-radius: 6px;
        }}
        
        ::-webkit-scrollbar-thumb:hover {{
            background: #6a6a6a;
        }}
        
        @media print {{
            body {{
                background: white;
            }}
            .controls, .btn {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🏰 Dungeon Level {level_num + 1} 🏰</h1>
        <div class="subtitle">Advanced Dungeons & Dragons Random Dungeon</div>
        
        <div class="controls">
            <button class="btn" onclick="zoomIn()">🔍 Zoom In</button>
            <button class="btn" onclick="zoomOut()">🔍 Zoom Out</button>
            <button class="btn" onclick="resetZoom()">↺ Reset View</button>
            <button class="btn" onclick="toggleGrid()">⊞ Toggle Grid</button>
            <button class="btn" onclick="window.print()">🖨️ Print</button>
        </div>
        
        <div class="map-container">
            <div class="map-wrapper">
                <svg id="dungeonMap" width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
"""
    
    # Generate SVG cells
    for j in range(downlist[down].shape[1]):
        for i in range(downlist[down].shape[0]):
            cell_value = downlist[down][i, j, 0]
            x = i * cell_size
            y = j * cell_size
            
            # Determine cell color and styling
            fill_color, stroke_color = get_cell_colors(cell_value)
            
            # Create cell with tooltip
            cell_id = f"cell_{i}_{j}"
            tooltip_text = get_tooltip_text(cell_value, room_stack, i + xmin, j + ymin, 0 - down - 1)
            # Escape quotes in tooltip for HTML attribute
            tooltip_text_attr = tooltip_text.replace('"', '&quot;')
            
            output_html += f'                    <rect class="cell" id="{cell_id}" x="{x}" y="{y}" '
            output_html += f'width="{cell_size}" height="{cell_size}" '
            output_html += f'fill="{fill_color}" stroke="{stroke_color}" '
            output_html += f'data-tooltip="{tooltip_text_attr}"/>\n'
            
            # Add text label if not empty
            if cell_value != 'B':
                text_color = get_text_color(cell_value)
                # Truncate long labels for display and escape for SVG
                display_text = cell_value[:6] if len(cell_value) > 6 else cell_value
                display_text_escaped = html.escape(display_text)
                output_html += f'                    <text class="cell-text" x="{x + cell_size/2}" y="{y + cell_size/2}" '
                output_html += f'fill="{text_color}">{display_text_escaped}</text>\n'
    
    output_html += """                </svg>
            </div>
        </div>
        
        <div class="tooltip" id="tooltip"></div>
"""
    
    # Add legend
    output_html += generate_legend()
    
    # Add room details and statistics
    output_html += generate_room_details(room_stack, level_num)
    
    output_html += """    </div>
    
    <script>
        let currentZoom = 1;
        const zoomStep = 0.2;
        const minZoom = 0.5;
        const maxZoom = 3;
        let gridVisible = true;
        
        const mapWrapper = document.querySelector('.map-wrapper');
        const svg = document.getElementById('dungeonMap');
        const tooltip = document.getElementById('tooltip');
        
        function zoomIn() {
            if (currentZoom < maxZoom) {
                currentZoom += zoomStep;
                updateZoom();
            }
        }
        
        function zoomOut() {
            if (currentZoom > minZoom) {
                currentZoom -= zoomStep;
                updateZoom();
            }
        }
        
        function resetZoom() {
            currentZoom = 1;
            updateZoom();
        }
        
        function updateZoom() {
            svg.style.transform = `scale(${currentZoom})`;
            svg.style.transformOrigin = 'top left';
        }
        
        function toggleGrid() {
            gridVisible = !gridVisible;
            const cells = document.querySelectorAll('.cell');
            cells.forEach(cell => {
                cell.style.strokeOpacity = gridVisible ? '1' : '0.1';
            });
        }
        
        // Tooltip functionality
        svg.addEventListener('mousemove', function(e) {
            const target = e.target;
            if (target.classList.contains('cell')) {
                const tooltipText = target.getAttribute('data-tooltip');
                if (tooltipText && tooltipText !== 'Empty') {
                    tooltip.innerHTML = tooltipText;
                    tooltip.style.display = 'block';
                    tooltip.style.left = (e.pageX + 10) + 'px';
                    tooltip.style.top = (e.pageY + 10) + 'px';
                } else {
                    tooltip.style.display = 'none';
                }
            }
        });
        
        svg.addEventListener('mouseleave', function() {
            tooltip.style.display = 'none';
        });
        
        // Pan functionality
        let isPanning = false;
        let startX, startY, scrollLeft, scrollTop;
        const mapContainer = document.querySelector('.map-container');
        
        mapContainer.addEventListener('mousedown', function(e) {
            if (e.button === 1 || e.shiftKey) { // Middle mouse or shift+left
                isPanning = true;
                startX = e.pageX - mapContainer.offsetLeft;
                startY = e.pageY - mapContainer.offsetTop;
                scrollLeft = mapContainer.scrollLeft;
                scrollTop = mapContainer.scrollTop;
                mapContainer.style.cursor = 'grabbing';
                e.preventDefault();
            }
        });
        
        mapContainer.addEventListener('mousemove', function(e) {
            if (!isPanning) return;
            e.preventDefault();
            const x = e.pageX - mapContainer.offsetLeft;
            const y = e.pageY - mapContainer.offsetTop;
            const walkX = (x - startX) * 2;
            const walkY = (y - startY) * 2;
            mapContainer.scrollLeft = scrollLeft - walkX;
            mapContainer.scrollTop = scrollTop - walkY;
        });
        
        mapContainer.addEventListener('mouseup', function() {
            isPanning = false;
            mapContainer.style.cursor = 'default';
        });
        
        mapContainer.addEventListener('mouseleave', function() {
            isPanning = false;
            mapContainer.style.cursor = 'default';
        });
        
        // Zoom with mouse wheel
        mapContainer.addEventListener('wheel', function(e) {
            if (e.ctrlKey) {
                e.preventDefault();
                if (e.deltaY < 0) {
                    zoomIn();
                } else {
                    zoomOut();
                }
            }
        });
    </script>
</body>
</html>
"""
    
    return output_html


def get_cell_colors(cell_value):
    """Return fill and stroke colors for a cell based on its value."""
    # Default colors
    fill = '#1a1a1a'  # Dark background (empty/void)
    stroke = '#333333'
    
    if cell_value == 'B':
        # Black/void
        fill = '#0a0a0a'
        stroke = '#000000'
    elif cell_value == 'O':
        # Outside entrance - green
        fill = '#2d5016'
        stroke = '#4a7c2a'
    elif 'R' in cell_value:
        # Room - gray with potential treasure colors
        if 'c' in cell_value:
            fill = '#8b4513'  # Copper
        elif 'g' in cell_value:
            fill = '#b8860b'  # Gold
        elif 'p' in cell_value:
            fill = '#c0c0c0'  # Platinum
        elif 's' in cell_value and 'sd' not in cell_value:
            fill = '#778899'  # Silver
        elif 'e' in cell_value:
            fill = '#9acd32'  # Electrum
        elif 'G' in cell_value:
            fill = '#00ced1'  # Gems
        elif 'j' in cell_value:
            fill = '#dc143c'  # Jewellery
        elif 'M' in cell_value:
            fill = '#ff1493'  # Magic
        elif 'm' in cell_value:
            fill = '#8b0000'  # Monster - dark red
        else:
            fill = '#4a4a4a'  # Regular room
        stroke = '#6a6a6a'
    elif 'C' in cell_value:
        # Corridor
        fill = '#2f2f2f'
        stroke = '#4a4a4a'
    elif 'D' in cell_value:
        # Dead end
        fill = '#654321'
        stroke = '#8b5a2b'
    elif 'CH' in cell_value:
        # Chasm
        fill = '#1c1c1c'
        stroke = '#3c3c3c'
    elif any(x in cell_value for x in ['P', 'L', 'W', 'S', 'br', 'bn', 'bo', 'ri']):
        # Water features
        fill = '#1e3a5f'
        stroke = '#2e5a8f'
    elif any(x in cell_value for x in ['st', 'ch', 'cm', 'td']):
        # Vertical movement (stairs, chutes, etc.)
        fill = '#8b4789'
        stroke = '#ab67a9'
    elif any(x in cell_value for x in ['pi', 'pt', 'ps', 'pc', 'el', 'ar', 'sp', 'df', 'sf', 'gs', 'bw', 'ol']):
        # Traps
        fill = '#8b0000'
        stroke = '#cd0000'
    
    return fill, stroke


def get_text_color(cell_value):
    """Return appropriate text color for readability."""
    # Check if cell has treasure markers
    if any(x in cell_value for x in ['c', 'g', 'p', 's', 'e', 'G', 'j', 'M']):
        return '#ffffff'
    elif 'm' in cell_value:
        return '#ffff00'
    else:
        return '#e0e0e0'


def get_tooltip_text(cell_value, room_stack, x, y, z):
    """Generate tooltip text for a cell."""
    if cell_value == 'B':
        return 'Empty'
    
    tooltip = f"<strong>Position:</strong> ({x}, {y}, {z})<br>"
    
    if cell_value == 'O':
        tooltip += "<strong>Type:</strong> Outside Entrance"
    elif 'R' in cell_value:
        # Extract room number
        room_num = ''.join(filter(str.isdigit, cell_value))
        if room_num and 'shape_dict' in room_stack:
            try:
                room_num = int(room_num)
                if room_num in room_stack['shape_dict']:
                    room = room_stack['shape_dict'][room_num]
                    tooltip += f"<strong>Type:</strong> Room #{room_num}<br>"
                    
                    if 'contents' in room and 'empty' not in room['contents']:
                        if 'monster' in room['contents']:
                            monster = room['contents']['monster']
                            monster_type = sanitize_for_html(monster.get('type', 'Unknown'))
                            monster_no = sanitize_for_html(monster.get('No', '?'))
                            tooltip += f"<span class='monster'>👹 Monster: {monster_type}</span><br>"
                            tooltip += f"<span class='monster'>Number: {monster_no}</span><br>"
                        
                        if 'treasure' in room['contents']:
                            treasure = room['contents']['treasure']['type']
                            has_treasure = any(treasure.get(k, 0) > 0 for k in treasure)
                            if has_treasure:
                                tooltip += "<span class='treasure'>💰 Treasure:</span><br>"
                                for coin_type in ['copper', 'silver', 'electrum', 'gold', 'platinum']:
                                    if treasure.get(coin_type, 0) > 0:
                                        coin_amount = sanitize_for_html(treasure[coin_type])
                                        tooltip += f"<span class='treasure'>  {coin_type.title()}: {coin_amount}</span><br>"
                                if treasure.get('gems', 0) > 0:
                                    gems_amount = sanitize_for_html(treasure['gems'])
                                    tooltip += f"<span class='treasure'>  💎 Gems: {gems_amount}</span><br>"
                                if treasure.get('jewellery', 0) > 0:
                                    jewellery_amount = sanitize_for_html(treasure['jewellery'])
                                    tooltip += f"<span class='treasure'>  📿 Jewellery: {jewellery_amount}</span><br>"
                                if treasure.get('magic', 0) > 0:
                                    magic_amount = sanitize_for_html(treasure['magic'])
                                    tooltip += f"<span class='treasure'>  ✨ Magic Items: {magic_amount}</span><br>"
                    else:
                        tooltip += "Empty Room"
                else:
                    tooltip += f"<strong>Type:</strong> Room #{room_num}"
            except:
                tooltip += "<strong>Type:</strong> Room"
        else:
            tooltip += "<strong>Type:</strong> Room"
    elif 'C' in cell_value:
        tooltip += "<strong>Type:</strong> Corridor"
        if 'd' in cell_value:
            tooltip += " (with door)"
    elif 'D' in cell_value:
        tooltip += "<strong>Type:</strong> Dead End"
    elif 'CH' in cell_value:
        tooltip += "<strong>Type:</strong> Chasm"
    elif 'st' in cell_value:
        tooltip += "<strong>Type:</strong> Stairs"
    elif 'wm' in cell_value:
        tooltip += "<strong>Type:</strong> Wandering Monster"
    
    if 'sd' in cell_value:
        tooltip += "<br>🔒 Secret Door"
    
    return tooltip


def generate_legend():
    """Generate the legend section."""
    legend_items = [
        ('#2d5016', 'Outside Entrance'),
        ('#4a4a4a', 'Room/Chamber'),
        ('#2f2f2f', 'Corridor/Passage'),
        ('#654321', 'Dead End'),
        ('#1e3a5f', 'Water (Pool/Lake)'),
        ('#1c1c1c', 'Chasm'),
        ('#8b4789', 'Stairs/Vertical'),
        ('#8b0000', 'Traps / Monsters'),
        ('#8b4513', 'Copper Treasure'),
        ('#778899', 'Silver Treasure'),
        ('#9acd32', 'Electrum Treasure'),
        ('#b8860b', 'Gold Treasure'),
        ('#c0c0c0', 'Platinum Treasure'),
        ('#00ced1', 'Gems'),
        ('#dc143c', 'Jewellery'),
        ('#ff1493', 'Magic Items'),
    ]
    
    output_html = """
        <div class="legend">
            <h3>📜 Legend</h3>
            <div class="legend-grid">
"""
    
    for color, description in legend_items:
        output_html += f"""
                <div class="legend-item">
                    <div class="legend-color" style="background-color: {color};"></div>
                    <span>{description}</span>
                </div>
"""
    
    output_html += """
            </div>
        </div>
"""
    
    return output_html


def generate_room_details(room_stack, level_num):
    """Generate detailed room information."""
    output_html = """
        <div class="room-details">
            <h3>🗝️ Room Details</h3>
"""
    
    if 'shape_dict' not in room_stack:
        output_html += "<p>No rooms on this level.</p>"
    else:
        room_count = 0
        monster_count = 0
        treasure_found = False
        
        for room_num in room_stack['shape_dict']:
            room = room_stack['shape_dict'][room_num]
            keylist = list(room_stack[room_num].keys())
            
            # Check if room is on this level
            if abs(keylist[0][2]) == level_num + 1:
                room_count += 1
                
                output_html += f"""
            <div class="room-entry">
                <div class="room-title">Room #{room_num}</div>
                <div class="room-content">
"""
                
                if 'empty' in room['contents']:
                    output_html += "<p>This room is empty.</p>"
                else:
                    contents = room['contents']
                    
                    if 'monster' in contents:
                        monster_count += 1
                        monster = contents['monster']
                        monster_type = sanitize_for_html(monster.get('type', 'Unknown'))
                        monster_no = sanitize_for_html(monster.get('No', '?'))
                        monster_xp = sanitize_for_html(monster.get('XP', 0))
                        output_html += f"<p><strong class='monster'>👹 Monster:</strong> {monster_type}</p>"
                        output_html += f"<p><strong class='monster'>Number:</strong> {monster_no}</p>"
                        output_html += f"<p><strong class='monster'>XP Value:</strong> {monster_xp} each</p>"
                        
                        if 'lair' in monster:
                            lair_chance = sanitize_for_html(monster['lair'])
                            output_html += f"<p><strong>Lair Chance:</strong> {lair_chance}</p>"
                    
                    if 'treasure' in contents:
                        treasure = contents['treasure']['type']
                        has_treasure = any(treasure.get(k, 0) > 0 for k in treasure)
                        
                        if has_treasure:
                            treasure_found = True
                            output_html += "<p><strong class='treasure'>💰 Treasure:</strong></p>"
                            output_html += "<div class='stats-grid'>"
                            
                            for coin_type in ['copper', 'silver', 'electrum', 'gold', 'platinum']:
                                if treasure.get(coin_type, 0) > 0:
                                    coin_amount = sanitize_for_html(treasure[coin_type])
                                    output_html += f"""
                                <div class='stat-item'>
                                    <div class='stat-label'>{coin_type.title()}</div>
                                    <div class='stat-value'>{coin_amount}</div>
                                </div>
"""
                            
                            if treasure.get('gems', 0) > 0:
                                gems_amount = sanitize_for_html(treasure['gems'])
                                output_html += f"""
                                <div class='stat-item'>
                                    <div class='stat-label'>💎 Gems</div>
                                    <div class='stat-value'>{gems_amount}</div>
                                </div>
"""
                            
                            if treasure.get('jewellery', 0) > 0:
                                jewellery_amount = sanitize_for_html(treasure['jewellery'])
                                output_html += f"""
                                <div class='stat-item'>
                                    <div class='stat-label'>📿 Jewellery</div>
                                    <div class='stat-value'>{jewellery_amount}</div>
                                </div>
"""
                            
                            if treasure.get('magic', 0) > 0:
                                magic_amount = sanitize_for_html(treasure['magic'])
                                output_html += f"""
                                <div class='stat-item'>
                                    <div class='stat-label'>✨ Magic Items</div>
                                    <div class='stat-value'>{magic_amount}</div>
                                </div>
"""
                            
                            output_html += "</div>"  # Close stats-grid
                            
                            # Storage and protection
                            if 'store' in contents['treasure']:
                                store_info = sanitize_for_html(contents['treasure']['store'])
                                output_html += f"<p><strong>Stored in:</strong> {store_info}</p>"
                            
                            if 'protection' in contents['treasure']:
                                prot = contents['treasure']['protection']
                                prot_type = sanitize_for_html(prot)
                                output_html += f"<p><strong>Protection:</strong> {prot_type.title()}</p>"
                                if prot in contents['treasure']:
                                    prot_detail = sanitize_for_html(contents['treasure'][prot])
                                    output_html += f"<p><em>{prot_detail}</em></p>"
                    
                    if 'trap' in contents:
                        trap_info = sanitize_for_html(contents['trap'])
                        output_html += f"<p><strong>⚠️ Trap:</strong> {trap_info}</p>"
                
                output_html += """
                </div>
            </div>
"""
        
        # Summary
        if room_count > 0:
            output_html += f"""
            <div class="info-panel" style="margin-top: 20px;">
                <div class="info-card">
                    <h3>📊 Level Summary</h3>
                    <div class="stats-grid">
                        <div class="stat-item">
                            <div class="stat-label">Total Rooms</div>
                            <div class="stat-value">{room_count}</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-label">Rooms with Monsters</div>
                            <div class="stat-value">{monster_count}</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-label">Treasure Found</div>
                            <div class="stat-value">{'Yes' if treasure_found else 'No'}</div>
                        </div>
                    </div>
                </div>
            </div>
"""
    
    output_html += """
        </div>
"""
    
    return output_html
