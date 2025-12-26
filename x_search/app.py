from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy database of search results
SEARCH_DATABASE = [
    {
        "title": "Introduction to Python",
        "url": "https://www.python.org/about/gettingstarted/",
        "description": "Python is a powerful and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open."
    },
    {
        "title": "Flask Documentation",
        "url": "https://flask.palletsprojects.com/",
        "description": "Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy."
    },
    {
        "title": "Artificial Intelligence - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "description": "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans."
    },
    {
        "title": "Machine Learning Course",
        "url": "https://www.coursera.org/learn/machine-learning",
        "description": "Machine learning is the science of getting computers to act without being explicitly programmed."
    },
    {
        "title": "Google Search",
        "url": "https://www.google.com",
        "description": "Search the world's information, including webpages, images, videos and more."
    }
]

def search_logic(query):
    query = query.lower()
    results = []
    for item in SEARCH_DATABASE:
        if query in item['title'].lower() or query in item['description'].lower():
            results.append(item)
    return results

def generate_ai_summary(query, results):
    if not results:
        return f"I couldn't find any information about '{query}' in my database."

    # Mock AI logic: simplistic summarization
    summary_text = "Based on the search results, here is a quick summary. "

    if "python" in query.lower():
        summary_text += "Python is a popular programming language known for its simplicity and versatility. It is widely used in web development, data science, and AI."
    elif "ai" in query.lower() or "intelligence" in query.lower():
        summary_text += "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. It encompasses subfields like machine learning and deep learning."
    elif "flask" in query.lower():
        summary_text += "Flask is a micro web framework written in Python. It's classified as a microframework because it does not require particular tools or libraries."
    else:
        summary_text += "The search results provide various resources. The top result mentions: " + results[0]['description']

    return summary_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return render_template('index.html')

    results = search_logic(query)
    ai_summary = generate_ai_summary(query, results)

    return render_template('results.html', query=query, results=results, ai_summary=ai_summary)

from flask import redirect

@app.route('/feeling-ai')
def feeling_ai():
    # Mock "I'm Feeling Lucky" behavior: redirect to a random or specific AI topic
    # Using a 302 Found redirect
    return redirect('/search?q=Artificial+Intelligence', code=302)

if __name__ == '__main__':
    app.run(debug=False)
