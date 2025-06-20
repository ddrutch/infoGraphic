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

"""Constants for infographic generator."""

from enum import Enum

class SocialMediaPlatform(str, Enum):
    GENERAL = "General"
    WHATSAPP = "WhatsApp"
    TWITTER = "Twitter"
    DISCORD = "Discord"
    REDDIT = "Reddit"

# Platform-specific dimensions (width, height)
PLATFORM_DIMENSIONS = {
    SocialMediaPlatform.GENERAL: (1920, 1080),
    SocialMediaPlatform.WHATSAPP: (1080, 1920),
    SocialMediaPlatform.TWITTER: (1200, 675),
    SocialMediaPlatform.DISCORD: (1080, 720),
    SocialMediaPlatform.REDDIT: (1080, 1080),
}

# Design constants
MAX_SLIDES = 10
MAX_ELEMENTS_PER_SLIDE = 8
FONT_CHOICES = ["Roboto", "Open Sans", "Montserrat", "Lato", "Poppins"]
COLOR_PALETTES = {
    "vibrant": ["#FF6B6B", "#4ECDC4", "#FFE66D", "#1A535C"],
    "professional": ["#2E4053", "#048BA8", "#99C24D", "#F18F01"],
    "minimal": ["#FFFFFF", "#F5F5F5", "#E0E0E0", "#212121"]
}

# API configuration
MAX_GENERATIVE_IMAGES = 2
MAX_WEB_IMAGES = 5
API_RETRY_ATTEMPTS = 2