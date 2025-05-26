from traffic import traffic_network

def print_flow(flow_value, flow_dict, title):
    print(f"\n{title}: {flow_value}00 véhicules/heure")
    print("\nRépartition du flux :")
    for u in sorted(flow_dict):
        for v in sorted(flow_dict[u]):
            if flow_dict[u][v] > 0:
                print(f"{u:5} -> {v:5} : {flow_dict[u][v]:2}00 véhicules/heure")

def main():
    print("=== Analyse du réseau routier ===")
    
    # Cas sans contraintes sur les villes
    flow_value, flow_dict = traffic_network.max_vehicule()
    print_flow(flow_value, flow_dict, "Débit maximal sans contraintes sur les villes")
    
    # Cas avec contraintes sur les villes
    flow_value, flow_dict = traffic_network.max_vehicule_avec_flux()
    print_flow(flow_value, flow_dict, "Débit maximal avec contraintes sur les villes")

if __name__ == "__main__":
    main()