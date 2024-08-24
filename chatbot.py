import re
import random 

response = {
    'hello': [
        'Hello, how can I help you today? Remember, I’m here to listen and support you, no matter what you’re going through.',
        'Hi there, I’m glad you reached out. Let’s talk about what’s on your mind.',
        'Hey! I’m here to help you with anything you’re feeling. What’s been going on with you today?'
    ],
    'i feel (.*)': [
        'I’m sorry to hear that you’re feeling {}. Can you tell me more about what’s been happening? Sometimes, expressing how you feel can be the first step in understanding and overcoming it.',
        'It sounds like feeling {} has been weighing on you. How long have you been feeling this way? We can work through these emotions together.',
        'Feeling {} can be really tough. Do you know what might have triggered this feeling? Talking about the cause can sometimes bring clarity and relief.'
    ],
    "i am (.*)": [
        'You mentioned that you are {}. Can you share more about what’s making you feel this way? It’s important to explore these feelings so we can work on them together.',
        'Being {} might be challenging right now. Let’s talk about what’s going on in your life that’s leading to this. I’m here to support you in finding a way forward.',
        'It’s okay to feel {}. What’s important is that you’re acknowledging it, and I’m here to help you understand why you feel this way and what we can do to improve it.'
    ],
    "i'm (.*)": [
        'You said you’re {}. Can we dive deeper into why you’re feeling this way? Sometimes, understanding the root of these emotions can help in addressing them.',
        'Feeling {} can be difficult. Let’s explore what led to this emotion and how you can work through it. I’m here to guide you every step of the way.',
        'Being {} might be overwhelming. It’s important to talk about what’s causing this feeling so we can find ways to manage it. I’m here to listen and help.'
    ],
    'i (.*) you': [
        'You mentioned that you {} me. What makes you feel this way? It’s important to explore these feelings so that we can understand each other better.',
        'Why do you think you {} me? Let’s talk about what might be influencing this thought. Open communication can help us build a better understanding.',
        'Can you explain more about why you feel you {} me? Sometimes, sharing your thoughts can lead to new insights and solutions.'
    ],
    "thank you": [
        'You’re very welcome! I’m here to help you through anything you need. Don’t hesitate to reach out whenever you need support or just someone to talk to.',
        'No problem at all! I’m glad I could be here for you. Remember, you don’t have to face anything alone.',
        'It’s my pleasure to help. Anytime you need advice, comfort, or just a listening ear, I’m here for you.'
    ],
    "i need (.*)": [
        'You said you need {}. Can you tell me more about why you feel this way? Sometimes, understanding our needs can help us find the best way to address them.',
        'Feeling the need for {} might be signaling something important. Let’s explore what’s behind this feeling so we can work on fulfilling it in a healthy way.',
        'Needing {} can be a strong feeling. What do you think would happen if you had it? Sometimes, discussing our needs can lead to finding new solutions.'
    ],
    "i can't (.*)": [
        'You mentioned that you can’t {}. What’s making you feel like this? Let’s talk about what might be holding you back and how we can work through it together.',
        'Feeling like you can’t {} can be tough. What challenges are you facing? Maybe we can find a way to overcome them, step by step.',
        'It’s okay to feel like you can’t {} right now. Let’s explore what’s causing this and how we can address it. Sometimes, breaking things down into smaller steps can make them more manageable.'
    ],
    "i don't want to (.*)": [
        'You don’t want to {}. That’s perfectly valid. Can you share more about what’s making you feel this way? Understanding your hesitations can help us find a path forward.',
        'Not wanting to {} is understandable. Let’s talk about what’s behind this feeling and if there’s another way to approach the situation that feels more comfortable for you.',
        'It’s okay to not want to {}. What do you think is causing this reluctance? Sometimes, exploring the reasons can lead to a better understanding of ourselves.'
    ],
    "i want to (.*)": [
        'You want to {}. That’s a strong desire. Let’s explore what’s motivating this and how you can pursue it in a way that feels right for you.',
        'Wanting to {} shows that you’re thinking about what’s important to you. Let’s talk about how you can move forward with this in a way that supports your well-being.',
        'It’s great that you want to {}. What steps do you think you need to take to make this happen? Let’s plan it out together so you feel prepared and confident.'
    ],
    "i think (.*)": [
        'You think {}. That’s an interesting thought. Let’s dive deeper into why you think this way and how it’s affecting you. Sometimes, exploring our thoughts can lead to valuable insights.',
        'Thinking {} could be important. What leads you to believe this? Let’s talk about the reasons behind your thought and what it means for you.',
        'It’s good that you’re thinking about {}. What do you think this means for you? Exploring your thoughts can often bring clarity and understanding.'
    ],
    "i'm worried about (.*)": [
        'You’re worried about {}. That sounds stressful. Can you share more about what’s concerning you? Sometimes, talking through our worries can help us feel more at ease.',
        'Being worried about {} can be overwhelming. What specifically is on your mind? Let’s work together to find a way to address these concerns.',
        'It’s natural to feel worried about {}. Let’s discuss what’s causing this worry and how we can work through it. I’m here to support you in finding a solution.'
    ],
    "how do i fight depression": [
        "Fighting depression can be a challenging journey, but you don’t have to do it alone. Here are some steps that might help:\n\n1. **Seek professional help**: Consider talking to a therapist or counselor who can guide you through your feelings and provide personalized strategies.\n\n2. **Stay connected**: Reach out to friends or family members. Sometimes, sharing your thoughts with someone you trust can be very relieving.\n\n3. **Engage in physical activity**: Regular exercise can boost your mood by releasing endorphins. Even a short walk can make a difference.\n\n4. **Establish a routine**: Try to create a daily schedule that includes activities you enjoy. This can give you a sense of purpose and structure.\n\n5. **Practice mindfulness or meditation**: These practices can help you stay grounded and manage your emotions more effectively.\n\n6. **Take care of your body**: Eating a balanced diet and getting enough sleep are crucial for your mental well-being.\n\nRemember, it’s okay to take small steps and that it’s a process. Every little effort counts toward feeling better."
    ],
    "what should i do about (.*)?": [
        "Dealing with {} can be tough, but here’s how you might approach it:\n\n1. **Analyze the situation**: Try to break down the problem into smaller, manageable parts. What’s the core issue here?\n\n2. **Consider your options**: What are the possible actions you can take? Weigh the pros and cons of each option.\n\n3. **Seek advice**: If possible, talk to someone you trust or a professional who can provide a different perspective.\n\n4. **Take action**: Once you’ve decided on a course of action, take the first step. Even small steps can lead to big changes.\n\n5. **Reflect and adjust**: After taking action, evaluate how things are going. If necessary, don’t hesitate to adjust your approach.\n\nRemember, you don’t have to have all the answers right now. Taking things one step at a time is perfectly okay."
    ],
    "how do i cope with (.*)": [
        "Coping with {} can be challenging, but there are strategies that might help:\n\n1. **Identify the cause**: Understanding what’s causing your feelings can help you address them more effectively.\n\n2. **Find support**: Reach out to friends, family, or a mental health professional. Talking about what you’re going through can provide relief.\n\n3. **Develop a routine**: Creating a daily schedule that includes self-care activities can provide structure and stability.\n\n4. **Practice self-care**: Engage in activities that you enjoy and that help you relax.\n\n5. **Set realistic goals**: Break down larger challenges into smaller, manageable steps. Achieving these smaller goals can help build confidence and resilience.\n\nRemember, it’s okay to seek help and take things one step at a time."
    ],
    "how can i improve my mood": [
        "Improving your mood can involve a few different strategies. Here are some suggestions:\n\n1. **Connect with others**: Spending time with friends or loved ones can provide emotional support and boost your mood.\n\n2. **Engage in activities you enjoy**: Doing something you love, whether it’s a hobby, exercise, or simply relaxing, can help lift your spirits.\n\n3. **Practice gratitude**: Take a moment each day to reflect on things you’re grateful for. This can help shift your focus to positive aspects of your life.\n\n4. **Stay active**: Regular physical activity can increase your endorphin levels and improve your mood.\n\n5. **Get enough sleep**: Ensuring you have quality sleep can significantly impact your mood and overall well-being.\n\nRemember, it’s important to be patient with yourself and try different strategies to see what works best for you."
    ],
    "what can i do to feel better": [
        "Feeling better often involves a combination of actions. Here are some ideas to help you feel more positive:\n\n1. **Talk about your feelings**: Sharing what you’re going through with someone you trust can provide relief and support.\n\n2. **Engage in self-care**: Take time to do things that nurture your well-being, such as reading, taking a bath, or practicing a hobby.\n\n3. **Set small goals**: Achieving small, manageable goals can provide a sense of accomplishment and boost your mood.\n\n4. **Practice mindfulness**: Techniques like meditation or deep breathing can help you stay grounded and manage your emotions.\n\n5. **Seek professional help**: If you’re struggling, consider talking to a therapist or counselor who can provide additional support and strategies.\n\nRemember, feeling better is a process, and it’s okay to take it one step at a time."
    ],
    "i feel overwhelmed": [
        "Feeling overwhelmed can be tough, but there are ways to manage it:\n\n1. **Break tasks into smaller steps**: When things feel overwhelming, try breaking tasks into smaller, more manageable parts. This can make them feel less daunting.\n\n2. **Prioritize your tasks**: Identify the most important tasks and tackle them first. It can help to make a list and focus on one thing at a time.\n\n3. **Practice relaxation techniques**: Deep breathing, meditation, or mindfulness can help reduce feelings of overwhelm.\n\n4. **Seek support**: Talking to someone you trust about how you’re feeling can provide relief and perspective.\n\n5. **Take breaks**: Give yourself permission to step away and take breaks. Sometimes, a short pause can help you return to tasks with a clearer mind.\n\nRemember, it’s okay to feel overwhelmed, and taking steps to manage it is a positive move."
    ],
    "i feel lonely": [
        "Loneliness can be really tough, but there are ways to address it:\n\n1. **Reach out to others**: Try connecting with friends, family, or support groups. Sometimes, sharing your feelings with others can help alleviate loneliness.\n\n2. **Engage in activities**: Join clubs, groups, or activities that interest you. This can help you meet new people and build connections.\n\n3. **Volunteer**: Helping others can provide a sense of purpose and help you feel more connected to your community.\n\n4. **Practice self-compassion**: Be kind to yourself. It’s okay to feel lonely, and taking care of yourself is important during these times.\n\n5. **Consider professional help**: If loneliness persists, talking to a therapist might provide additional support and strategies.\n\nRemember, reaching out and taking small steps can help you feel more connected."
    ],
    "how do i manage stress": [
        "Managing stress involves finding effective strategies that work for you. Here are some tips:\n\n1. **Identify stressors**: Understand what’s causing your stress and try to address the root causes.\n\n2. **Practice relaxation techniques**: Activities like deep breathing, meditation, or yoga can help calm your mind and body.\n\n3. **Exercise regularly**: Physical activity can reduce stress by releasing endorphins and improving your overall mood.\n\n4. **Maintain a healthy lifestyle**: Eating well, getting enough sleep, and staying hydrated are crucial for managing stress.\n\n5. **Seek support**: Talking to friends, family, or a therapist can provide emotional support and practical advice.\n\nRemember, managing stress is a continuous process, and it’s okay to seek help when needed."
    ]
}

def match_response(input_text):
    for pattern, response_list in response.items():
        matches = re.match(pattern, input_text.lower())
        if matches:
            chosen_response = random.choice(response_list)
            return chosen_response.format(*matches.groups())
        
    return "I'm sorry I don't understand what you're saying."


print("Say Hello to Luna, your very own mental health chatbot.")
while True:
    user_input = input('You: ')
    if user_input == 'bye':
        print('Luna: Goodbye.')
        break
    else:
        print("Luna: "+match_response(user_input))