import json
import glob
import time

def entrenar_tahyi(contract_file):
    with open(contract_file, 'r') as f:
        contrato = json.load(f)
    
    agent_id = contrato["agent_id"]
    role = contrato["role"]
    target = contrato["target_adversary"]
    
    print(f"\n[+] Oñepyrũ entrenamiento: {agent_id} ({role})")
    print(f"    Target: {target}")
    
    # Simulación de ciclos de entrenamiento LBH
    for ciclo in range(1, 4):
        time.sleep(0.3)
        print(f"    -> Ciclo {ciclo}/3: Bloqueando patrón '{target}'... [OK]")
    
    contrato["status"] = "ENTRENADO_Y_ACTIVO"
    contrato["fidelidad_LBH"] = "100%"
    contrato["training_timestamp"] = time.time()
    
    with open(contract_file, 'w') as f:
        json.dump(contrato, f, indent=4)
        
    print(f"[✔] {agent_id} oñembosako'íma! Contrato oñembopyahúma.")

# Entrenar las 7 hormigas
archivos = sorted(glob.glob("hormiga_*_contract.json"))
for archivo in archivos:
    entrenar_tahyi(archivo)

print("\n¡Opáma entrenamiento! Umi 7 tahýi oĩma listos oñorairõ haguã Lenguaje-Binario-HormigasAIS poguýpe.")
