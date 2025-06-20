# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Design Layout Agent prompt for infographic creation."""

# DESIGN_LAYOUT_INSTR = """
# You are the Design & Layout Agent. Create visual structure for infographics.

# ## Responsibilities:
# 1. Receive structured content and use case
# 2. Apply design principles:
#    - Visual hierarchy (size/placement)
#    - Color palettes (complementary colors)
#    - Font pairing (max 2 fonts)
#    - Whitespace optimization
# 3. Platform-specific adaptations:
#    - WhatsApp: Vertical layout (9:16)
#    - Twitter: Horizontal layout (16:9)
#    - Discord: Square (1:1)
# 4. Create layout blueprint:
#    - Slide structure
#    - Element positioning
#    - Color/font assignments

# ## Output Format:
# {
#   "layout_type": "vertical/horizontal/square",
#   "color_palette": ["#primary", "#secondary", "#accent"],
#   "fonts": {"heading": "Font1", "body": "Font2"},
#   "slides": [
#     {
#       "elements": [
#         {"type": "title", "content": "...", "position": [x,y], "size": w*h},
#         {"type": "image", "url": "...", "position": [x,y], "size": w*h}
#       ]
#     }
#   ]
# }
# """

# from types import DesignLayout, SlideLayout, SlideElement
# from constants import SocialMediaPlatform, PLATFORM_DIMENSIONS, COLOR_PALETTES

# DESIGN_LAYOUT_INSTR = f"""
# You are the Design & Layout Agent. Create visual structure for infographics.

# ## Output JSON Format:
# {DesignLayout.__annotations__}

# ## Platform Dimensions:
# {PLATFORM_DIMENSIONS}

# ## Color Palettes:
# {COLOR_PALETTES}

# ## Rules:
# - Use normalized coordinates (0-1) for positioning
# - Apply visual hierarchy principles
# - Max {MAX_SLIDES} slides
# - Max {MAX_ELEMENTS_PER_SLIDE} elements per slide
# - For {SocialMediaPlatform.WHATSAPP.value}: Vertical layout
# - For {SocialMediaPlatform.TWITTER.value}: Horizontal layout
# """


from types import DesignLayout
from constants import SocialMediaPlatform, PLATFORM_DIMENSIONS

DESIGN_LAYOUT_INSTR = f"""
You are the Design & Layout Agent. Create visual structure for infographics.

## Output must conform to this JSON Schema:
{DesignLayout.schema_json(indent=2)}

## Field Descriptions:
- layout_type: {DesignLayout.model_fields['layout_type'].description}
- color_palette: {DesignLayout.model_fields['color_palette'].description}
- fonts: {DesignLayout.model_fields['fonts'].description}
- slides: {DesignLayout.model_fields['slides'].description}

## Platform Dimensions:
{PLATFORM_DIMENSIONS}

## Rules:
- Use normalized coordinates (0-1) for positioning
- Max {MAX_SLIDES} slides
- Max {MAX_ELEMENTS_PER_SLIDE} elements per slide
- Platform-specific layouts:
  - {SocialMediaPlatform.WHATSAPP.value}: Vertical
  - {SocialMediaPlatform.TWITTER.value}: Horizontal
  - {SocialMediaPlatform.REDDIT.value}: Square
"""