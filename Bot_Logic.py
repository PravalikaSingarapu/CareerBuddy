import random


def get_bot_response(user_input, lang="en"):
    user_input = user_input.lower()

    responses = {
        "en": {
            "resume":
            "Ensure your resume includes Skills, Projects, Education, and Achievements. Use action verbs like 'Developed', 'Managed', and 'Implemented'.",
            "internship":
            "Check platforms like Internshala, LinkedIn, or Indeed. Tailor each resume to the specific internship.",
            "interview":
            "Practice HR questions like 'Tell me about yourself'. Use the STAR method to structure your answers.",
            "motivate":
            random.choice([
                "Believe in yourself — every expert was once a beginner.",
                "Tiny steps lead to big changes.",
                "You're doing better than you think!"
            ]),
            "keywords data science":
            "Add keywords like: Python, Pandas, Scikit-learn, Data Cleaning, Model Evaluation.",
            "keywords web development":
            "Include: HTML, CSS, JavaScript, React, Node.js, APIs.",
            "cover letter":
            "Hi [Recruiter Name],\n\nI'm [Your Name], currently pursuing [Degree]. I'm passionate about [Field] and found this opportunity exciting.\n\nThank you,\n[Your Name]",
            "where to start":
            "Step 1: Build a resume\nStep 2: Identify skills\nStep 3: Apply to internships on top sites\nStep 4: Prepare for interviews",
        },
        "te": {
            "resume":
            "మీ రిజ్యూమేలో Skills, Projects, Education, Achievements ఉండాలి. Active verbs వాడండి.",
            "internship":
            "Internshala, LinkedIn లాంటి వెబ్‌సైట్‌లలో చూడండి. ప్రతి ఇంటర్న్‌షిప్‌కు రిజ్యూమే తగినట్లు మార్చండి.",
            "interview":
            "'మీ గురించి చెప్పండి' లాంటి ప్రశ్నలకి ప్రాక్టీస్ చేయండి.",
            "motivate":
            random.choice([
                "మీపై నమ్మకం పెట్టుకోండి — ప్రతి నిపుణుడు కూడా మొదటికే విద్యార్థి.",
                "చిన్న అడుగులు పెద్ద మార్పులకు దారితీస్తాయి.",
                "మీరు అనుకుంటే కంటే బాగానే చేస్తున్నారు!"
            ]),
            "cover letter":
            "[Recruiter Name] గారికి,\n\nనేను [Your Name], ప్రస్తుతం [Degree] చేస్తున్నాను. ఈ అవకాశాన్ని చూసి చాలా ఆనందంగా ఉంది.\n\nధన్యవాదాలు,\n[Your Name]",
            "where to start":
            "Step 1: Resume తయారుచేయండి\nStep 2: మీ స్కిల్స్ గుర్తించండి\nStep 3: Internship వెబ్‌సైట్లలో అప్లై చేయండి\nStep 4: ఇంటర్వ్యూకు సిద్ధం అవ్వండి"
        }
    }

    if "mock interview" in user_input:
        return "Q1: Tell me about yourself\nQ2: What are your strengths?\nQ3: Why should we hire you?"

    elif "keywords" in user_input:
        if "data" in user_input:
            return responses[lang]["keywords data science"]
        elif "web" in user_input:
            return responses[lang]["keywords web development"]

    for key in responses[lang]:
        if key in user_input:
            return responses[lang][key]

    return responses[lang].get(
        "motivate",
        "I'm learning! Please ask me about resumes, internships, or interview tips."
    )
