# StoryG
Customized GPT for Educational and Relatable Content for Children

## Overview
StoryG is a groundbreaking AI-driven platform designed to generate personalized educational and entertainment content for children. This application, leveraging the power of generative AI, specifically GPT models, enables parents and educators to create customized stories and learning materials. StoryG tailors its output to the individual needs and preferences of each child, taking into account factors such as age, interests, and specific educational goals.

## Hackathon product
Visit the StoryG GPT page to test and demo the tool: https://chat.openai.com/g/g-ZQcpJzoRV-storyg

## Hackathon video demo
[![StoryG GPT Project Video](http://img.youtube.com/vi/NQgcWb3Aohk/0.jpg)](http://www.youtube.com/watch?v=NQgcWb3Aohk "StoryG GPT Project Video")

## Hackathon presentation
https://drive.google.com/file/d/1tDAA43obncOxwfEp638zOKzBEnNLcKmB/view?usp=sharing



### Key Features
- **Personalized Story Generation**: Customizes stories based on a child's age, gender, and personal preferences.
- **Educational Content**: Designed to teach concepts across various subjects including art, science, and morality.
- **Interactive Learning**: Engages children through interactive quizzes and scenarios.
- **Multi-Format Support**: Offers content in diverse formats including text, picture books, audio books, and videos.
- **Parental Dashboard**: Provides a platform for parents to manage content and monitor their child's learning progress.


### Getting Started
#### Prerequisites
Python 3.8 or higher.
Virtual environment (recommended for development).
### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/storyg.git
2. **Navigate to the Project Directory**
    ```bash
    cd storyg
3. **Set Up a Virtual Environment (Optional)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
4. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
### Running the Application
#### Execute the application using:
  ```bash
    python src/main.py
```
### Usage
Include details on how to utilize the application, highlighting any UI/UX elements, command-line arguments, or necessary environmental variables.

#### Example
  ```python
    from storyg import StoryG

    story_generator = StoryG(age=7, gender='female', story_type='picture_book')
    story = story_generator.generate()
    print(story)
```

### Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. 
We are currently considering options to recreate StoryG using an open source model stack and invite the community to contribute and support us in this cause.

### Deployment
This application is not deployable in a production environment yet. It is accessible in the OpenAI GPT Store for use and testing as needed.

### Built With
- **Python** - Primary programming language
- **Flask** - Web framework used
- **OpenAI's GPT** - AI model for content generation
### Authors
- **Tanika Mehra** - Founding Team
- **Nazeer Kamdar** - Founding Team
- **Emma Xu** - Founding Team
- **Yimeng Li** - Founding Team

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments
Appreciation to anyone whose code was used
Inspiration sources
etc.
