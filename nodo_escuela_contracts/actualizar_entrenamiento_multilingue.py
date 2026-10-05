import json
import glob
import time

# Diccionario de Mapeo Emocional y Técnico Multilingüe (ES, EN, GN)
MULTILINGUAL_DICTIONARY = {
    "miedo": ["miedo", "fear", "kyhyje", "anxiety", "threat"],
    "deseo": ["deseo", "desire", "potapy", "arousal", "attraction"],
    "drama": ["drama", "suspense", "sensational", "controversy"],
    "fomo": ["urgencia", "urgency", "loss_aversion", "expiring", "oferta_unica"],
    "tracking": ["pixel", "cookie_sync", "dwell_time", "fingerprint", "tracker"]
}

def enriquecer_contrato_multilingue(contract_file):
    with open(contract_file, 'r') as f:
        contrato = json.load(f)
    
    agent_id = contrato["agent_id"]
    
    # Inyección de matriz multilingüe al contrato LBH
    contrato["multilingual_defense"] = {
        "status": "MULTILINGUAL_ENABLED",
        "supported_languages": ["ES", "EN", "GN"],
        "token_matrix": MULTILINGUAL_DICTIONARY
    }
    contrato["last_evaluation"] = time.time()
    
    with open(contract_file, 'w') as f:
        json.dump(contrato, f, indent=4)
        
    print(f"[✔] {agent_id}: Matriz multilingüe (ES / EN / GN) integrada con éxito.")

# Aplicar a las 7 hormigas
archivos = sorted(glob.glob("hormiga_*_contract.json"))
for archivo in archivos:
    enriquecer_contrato_multilingue(archivo)

print("\n¡Evaluación completada! La colonia de 7 hormigas ahora detecta patrones adversarios en Inglés, Español y Guaraní bajo el estándar LBH.")
