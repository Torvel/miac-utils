from flask import Flask, request, jsonify
import ipaddress
import datetime

app = Flask(__name__)

def mock_block_ip_in_paloalto(ip):
    """
    Simula el bloqueo de una IP en un firewall Palo Alto.
    Aquí podrías integrar la API real en el futuro.
    """
    timestamp = datetime.datetime.utcnow().isoformat()
    print(f"[MOCK] [{timestamp}] Bloqueando IP en PaloAlto: {ip}")
    
    # Simulación de resultado
    return {
        "status": "success",
        "action": "block",
        "firewall": "paloalto",
        "ip_blocked": ip,
        "timestamp": timestamp
    }

@app.route('/block_ip', methods=['POST', 'GET'])
def block_ip():
    # Obtener IP desde POST (JSON o form) o desde query string
    ip = request.values.get("ip")

    if not ip:
        return jsonify({"error": "Falta el parámetro 'ip'"}), 400

    # Validar IP
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return jsonify({"error": "Dirección IP no válida"}), 400

    # Ejecutar mock de bloqueo
    result = mock_block_ip_in_paloalto(ip)

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
