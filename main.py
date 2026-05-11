from flask import Flask, render_template_string
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Floating Design | Spots</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            background: #fff9e8;
            font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
            padding: 2rem;
            position: relative;
        }

        /* Spotted pattern: white, yellow, green */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            background-image: 
                radial-gradient(circle at 15% 25%, #ffffff 8px, transparent 8px),
                radial-gradient(circle at 85% 60%, #f9f3c1 12px, transparent 12px),
                radial-gradient(circle at 45% 80%, #d4e6b0 10px, transparent 10px),
                radial-gradient(circle at 70% 20%, #fff2b5 7px, transparent 7px),
                radial-gradient(circle at 30% 55%, #c8e6a5 9px, transparent 9px),
                radial-gradient(circle at 90% 90%, #fcf0c0 14px, transparent 14px),
                radial-gradient(circle at 5% 70%, #e2f0d0 6px, transparent 6px),
                radial-gradient(circle at 50% 10%, #ffffff 11px, transparent 11px);
            background-size: 200px 200px;
            background-repeat: repeat;
            opacity: 0.7;
        }

        .cards-container {
            max-width: 1200px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }

        .floating-card {
            display: flex;
            align-items: center;
            gap: 2rem;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(8px);
            border-radius: 32px;
            padding: 1.5rem 2rem;
            box-shadow: 0 20px 35px -12px rgba(0, 0, 0, 0.2),
                        0 0 0 1px rgba(255, 255, 255, 0.5) inset;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
            animation: float 4s infinite ease-in-out;
        }

        .floating-card:nth-child(1) { animation-delay: 0s; }
        .floating-card:nth-child(2) { animation-delay: 0.6s; }
        .floating-card:nth-child(3) { animation-delay: 1.2s; }
        .floating-card:nth-child(4) { animation-delay: 0.3s; }

        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
            100% { transform: translateY(0px); }
        }

        .floating-card:hover {
            transform: scale(1.01) translateY(-4px);
            box-shadow: 0 28px 40px -14px rgba(0, 0, 0, 0.3);
            background: rgba(255, 255, 255, 0.95);
        }

        .card-icon {
            flex-shrink: 0;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #f5e7b2, #d4e6b0);
            border-radius: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.8rem;
            box-shadow: 0 8px 14px rgba(0, 0, 0, 0.1);
        }

        .card-description {
            flex: 1;
        }

        .card-description h3 {
            font-size: 1.7rem;
            color: #3a5a2a;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        .card-description p {
            font-size: 1.1rem;
            color: #2c3e2a;
            line-height: 1.4;
        }

        @media (max-width: 700px) {
            .floating-card {
                flex-direction: column;
                text-align: center;
                padding: 1.5rem;
            }
            .card-description h3 {
                font-size: 1.4rem;
            }
            body {
                padding: 1rem;
            }
        }

        .page-title {
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
            z-index: 2;
            color: #2a5a2a;
            font-size: 2.2rem;
            font-weight: 500;
            text-shadow: 2px 2px 0 rgba(255,255,200,0.8);
        }
    </style>
</head>
<body>
    <div class="cards-container">
        <div class="page-title">✨ floating elements ✨</div>

        <div class="floating-card">
            <div class="card-icon">🌿</div>
            <div class="card-description">
                <h3>Fresh & organic</h3>
                <p>Soft white‑yellow‑green spots create a calming, nature‑inspired background. Each card floats gently.</p>
            </div>
        </div>

        <div class="floating-card">
            <div class="card-icon">☁️</div>
            <div class="card-description">
                <h3>Airy elevations</h3>
                <p>Cards hover with a subtle floating animation. Perfect for dashboards, portfolios, or mood boards.</p>
            </div>
        </div>

        <div class="floating-card">
            <div class="card-icon">🌟</div>
            <div class="card-description">
                <h3>Description beside icon</h3>
                <p>Each card pairs a visual icon with descriptive text on the same row — clear and modern.</p>
            </div>
        </div>

        <div class="floating-card">
            <div class="card-icon">🎨</div>
            <div class="card-description">
                <h3>Customizable spots</h3>
                <p>The background uses overlapping radial gradients. You can easily change colors, sizes, and density.</p>
            </div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
