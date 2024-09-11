

import streamlit as st
from streamlit.components.v1 import html

# Define the HTML, CSS, and JavaScript for typewriter animation
animation_code = """
<html>
<head>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            color: white;
            background: linear-gradient(90deg, #ff0000, #00ff00, #0000ff, #ffff00, #ff00ff); /* Colors for gradient */
            background-size: 500% 500%; /* Adjust for smooth transition */
            animation: gradient 10s ease infinite; /* Gradient animation */
            overflow-x: hidden; /* Prevent horizontal scroll */
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .container {
            text-align: center;
            padding: 50px;
            width: 100%; /* Full viewport width */
            box-sizing: border-box; /* Ensure padding is included in the width */
        }
        .typewriter {
            display: inline-block;
            white-space: nowrap;
            overflow: hidden;
            font-size: 24px;
            border-right: .15em solid orange; /* Typewriter cursor */
            animation: typing 6s steps(50, end), blink-caret .75s step-end infinite;
        }
        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }
        @keyframes blink-caret {
            from, to { border-color: transparent; }
            50% { border-color: orange; }
        }
        .logo {
            position: fixed;
            top: 10px;
            left: 10px;
            width: 100px; /* Adjust as needed */
            height: auto; /* Maintain aspect ratio */
            z-index: 10; /* Ensure logo is above other content */
        }
        /* Responsive adjustments */
        @media (max-width: 600px) {
            .typewriter {
                font-size: 18px; /* Smaller font size on small screens */
            }
            .container {
                padding: 20px; /* Reduce padding on small screens */
            }
            .logo {
                width: 80px; /* Smaller logo size on small screens */
            }
        }
    </style>
</head>
<body>
  
    <div class="container">
        <h1 style="color: #FF5733;">Under Construction</h1>
        <div class="typewriter">
            
            website is currently under construction. 
            <br>  Stay tuned! 
            <span style="font-size: 30px;">⌛</span>
        </div>
    </div>
</body>
</html>
"""

# Display the HTML and CSS using Streamlit's HTML component with adjusted height
html(animation_code, height=700)  # Adjust height if needed
