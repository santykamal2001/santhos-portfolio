export const mockData = {
  about: {
    description: "I’m a Software Engineer and AI/ML enthusiast with experience building intelligent, scalable, and user-centered solutions. My journey spans from designing accessible banking interfaces during my UI/UX internship to developing AI-driven projects such as soil type classification using deep learning, forest fire prediction with machine learning models, and a multilingual voice chatbot powered by RAG and GenAI."
  },
  
  timeline: [
    {
      type: "education",
      title: "M.Eng. in Computer Science",
      organization: "Oregon State University",
      period: "2024 - 2025",
      description: "Advanced studies in software engineering, machine learning, and system design with a GPA of 3.6.",
      achievements: [
        "Specialized in AI/ML applications and full-stack development",
        "Conducted research in biological network analysis and data processing",
        "Developed UX prototypes for mobile applications"
      ]
    },
    {
      type: "experience",
      title: "UI Developer Intern",
      organization: "Rumango Software & Consulting Services",
      period: "Feb 2023 - Jul 2023",
      description: "Developed full-stack solutions for international banking clients, focusing on transaction processing and system optimization.",
      achievements: [
        "Built scalable systems that improved transaction success rates by 25%",
        "Created internal tools and dashboards to streamline workflows",
        "Implemented CI/CD practices and automated testing frameworks",
        "Collaborated with cross-functional teams on critical banking infrastructure"
      ]
    },
    {
      type: "experience",
      title: "Web Developer Intern",
      organization: "The Sparks Foundation",
      period: "Sep 2021 - Oct 2021",
      description: "Developed a full-stack payment gateway solution with automated testing and monitoring capabilities.",
      achievements: [
        "Built secure payment processing system with RESTful APIs",
        "Implemented automated testing framework for quality assurance",
        "Created monitoring and validation tools for system reliability"
      ]
    },
    {
      type: "education",
      title: "B.E. in Computer Science",
      organization: "St. Joseph's College of Engineering",
      period: "2019 - 2023",
      description: "Undergraduate studies in computer science fundamentals with a GPA of 3.3.",
      achievements: [
        "Strong foundation in algorithms, data structures, and software engineering",
        "Developed multiple projects including ML models and web applications",
        "Active participation in coding competitions and technical workshops"
      ]
    }
  ],

  projects: [
    {
      title: "End-to-End Multilingual Voice Chatbot",
      description: "A comprehensive AI-powered chatbot system integrating Automatic Speech Recognition, Retrieval-Augmented Generation, and Text-to-Speech technologies for multilingual voice interactions.",
      technologies: ["React", "Python", "ChromaDB", "LangChain", "TensorFlow", "AWS"],
      github: "https://github.com/santykamal2001/multilingual-voice-chatbot",
      demo: null,
      icon: "🤖",
      highlights: [
        "Improved response accuracy by 30% through advanced RAG implementation",
        "Real-time voice processing with sub-second response times",
        "Support for multiple languages with seamless translation"
      ]
    },
    {
      title: "Real-Time Audio Transcription Pipeline",
      description: "Serverless architecture using AWS Lambda and API Gateway for scalable speech-to-text processing with real-time transcription capabilities and automated monitoring.",
      technologies: ["AWS Lambda", "API Gateway", "AWS Transcribe", "Python", "CloudWatch"],
      github: "https://github.com/santykamal2001/aws-transcription-service",
      demo: null,
      icon: "🎵",
      highlights: [
        "Fully serverless architecture for cost-effective scaling",
        "Real-time audio processing with automatic language detection",
        "Comprehensive monitoring and logging with AWS CloudWatch"
      ]
    },
    {
      title: "Disease Diagnosis System",
      description: "Modular backend system simulating real-time patient-doctor interactions with secure authentication, data validation, and comprehensive API endpoints for healthcare management.",
      technologies: ["Java", "MySQL", "Spring Boot", "RESTful APIs", "JUnit"],
      github: "https://github.com/santykamal2001/Disease-Diagnosis-System",
      demo: null,
      icon: "⚕️",
      highlights: [
        "Secure patient data management with HIPAA compliance considerations",
        "Modular architecture supporting multiple healthcare workflows",
        "Comprehensive automated testing suite for reliability"
      ]
    },
    {
      title: "Forest Fire Prediction Model",
      description: "Machine learning pipeline using Random Forest algorithm to predict forest fire occurrences with automated data preprocessing, model training, and web-based visualization dashboard.",
      technologies: ["Python", "Random Forest", "Pandas", "Scikit-learn", "Flask", "Matplotlib"],
      github: "https://github.com/santykamal2001/Forest_Fire_Predict_Random-Forest",
      demo: null,
      icon: "🔥",
      highlights: [
        "18% improvement in recall for early fire detection",
        "Automated data preprocessing pipeline for real-time predictions",
        "Interactive web dashboard for forest management teams"
      ]
    },
    {
      title: "Biological Network Analysis",
      description: "Advanced data processing framework for analyzing protein interaction networks using Markov Clustering and Molecular Complex Detection algorithms with visualization tools.",
      technologies: ["Python", "NetworkX", "Pandas", "Matplotlib", "Scikit-learn"],
      github: "https://github.com/santykamal2001/Biological_Network_Analysis.git",
      demo: null,
      icon: "🧬",
      highlights: [
        "80% reduction in computation time through optimization",
        "Advanced clustering algorithms for complex biological data",
        "Comprehensive visualization tools for research insights"
      ]
    },
    {
      title: "Soil Type Classification App",
      description: "Web application using Convolutional Neural Networks to classify soil types from image data, integrated with Django backend and React frontend for seamless user experience.",
      technologies: ["Django", "React", "CNN", "TensorFlow", "OpenCV", "PostgreSQL"],
      github: null,
      demo: null,
      icon: "🌱",
      highlights: [
        "High accuracy soil classification for agricultural applications",
        "Real-time image processing with instant results",
        "User-friendly interface for field researchers and farmers"
      ]
    }
  ],

  certifications: [
    {
      title: "Introduction to Data Analytics on Google Cloud",
      issuer: "Google Cloud",
      date: "March 2025",
      credentialId: "14423871",
      description: "Comprehensive certification covering data analytics fundamentals, cloud infrastructure, and big data processing on Google Cloud Platform.",
      skills: ["Google Cloud Platform", "BigQuery", "Data Analytics", "Cloud Computing"],
      verifyUrl: null
    },
    {
      title: "Accenture North America - Product Design Job Simulation",
      issuer: "Accenture via Forage",
      date: "August 2024",
      credentialId: "yXmqXy88LBA557eCx",
      description: "Practical simulation focusing on product design methodologies, user research, and design thinking processes used in enterprise environments.",
      skills: ["Product Design", "User Research", "Design Thinking", "Prototyping"],
      verifyUrl: null
    },
    {
      title: "JPMorgan Chase & Co. - Agile Job Simulation",
      issuer: "JPMorgan Chase via Forage",
      date: "August 2024",
      credentialId: "sWsiEPQFbgEY3MPm3",
      description: "Hands-on experience with Agile methodologies, sprint planning, and collaborative development practices in financial services environment.",
      skills: ["Agile Methodology", "Scrum", "Sprint Planning", "Team Collaboration"],
      verifyUrl: null
    },
    {
      title: "Web Development Course",
      issuer: "SmartKnower",
      date: "July 2021",
      credentialId: null,
      description: "Comprehensive web development training covering modern frontend and backend technologies, responsive design, and best practices.",
      skills: ["HTML5", "CSS3", "JavaScript", "Responsive Design", "Web Development"],
      verifyUrl: null
    }
  ]
};