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

"""Common data schema and types for infographic generator agents."""

from typing import List, Dict, Tuple, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field

# Convenient declaration for controlled generation
json_response_config = types.GenerateContentConfig(
    response_mime_type="application/json"
)

class ContentType(str, Enum):
    TITLE = "title"
    SUBTITLE = "subtitle"
    BODY = "body"
    BULLET = "bullet"
    IMAGE = "image"
    CHART = "chart"

class ImageSource(str, Enum):
    WEB = "web"
    GENERATIVE = "generative"

class ImageAsset(BaseModel):
    """Represents a visual asset for infographics"""
    url: str = Field(description="Publicly accessible URL of the image")
    type: str = Field(description="Asset type: logo/character/background/border")
    source: ImageSource = Field(description="How the image was sourced")
    description: str = Field(description="Brief caption for accessibility")

class TextElement(BaseModel):
    """Represents a text element in the infographic"""
    content: str = Field(description="Actual text content")
    style: str = Field(description="Style reference from DesignLayout")

class SlideElement(BaseModel):
    """Represents an element on a slide"""
    element_id: str = Field(description="Unique identifier for the element")
    type: ContentType = Field(description="Type of content element")
    content: Union[str, ImageAsset] = Field(description="Text or image content")
    position: Tuple[float, float] = Field(
        description="Normalized position (x,y) from 0.0 to 1.0"
    )
    size: Tuple[float, float] = Field(
        description="Normalized size (width,height) from 0.0 to 1.0"
    )

class SlideLayout(BaseModel):
    """Layout definition for a single slide"""
    background: Optional[str] = Field(
        description="Background color or image URL"
    )
    elements: List[SlideElement] = Field(
        description="Elements contained in the slide"
    )

class DesignLayout(BaseModel):
    """Complete design specification for infographic"""
    layout_type: str = Field(description="vertical/horizontal/square")
    color_palette: List[str] = Field(
        description="Primary color scheme in hex codes"
    )
    fonts: Dict[str, str] = Field(
        description="Font assignments: heading, body, etc."
    )
    slides: List[SlideLayout] = Field(
        description="Ordered list of slide layouts"
    )

class TextStyle(BaseModel):
    """Text formatting specification"""
    font_family: str = Field(description="Font name")
    font_size: int = Field(description="Font size in points")
    color: str = Field(description="Text color in hex code")
    bold: bool = Field(description="Whether text is bold")
    italic: bool = Field(description="Whether text is italicized")
    alignment: str = Field(description="LEFT/CENTER/RIGHT")

class AnalysisResult(BaseModel):
    """Output from Content Analysis Agent"""
    title: str = Field(description="Main title of infographic")
    subtopics: List[Dict[str, Union[str, List[str]]]] = Field(
        description="Structured content with headings and points"
    )
    keywords: List[str] = Field(
        description="Key terms for image sourcing"
    )
    numerical_data: List[Dict[str, Union[str, float]]] = Field(
        description="Extracted numbers and statistics"
    )
    style_suggestion: str = Field(
        description="Recommended design style"
    )