from traffic import traffic_network

def main():
    flow_value, flow_dict = traffic_network.max_vehicule()
    print("Débit maximal de véhicules entre E et S :", flow_value, " 000 véhicules/heure")
    print("\nRépartition du flux :")
    for u in flow_dict:
        for v in flow_dict[u]:
            if flow_dict[u][v] > 0:
                print(f"{u} -> {v} : {flow_dict[u][v]} 000 véhicules/heure")

if __name__ == "__main__":
    main()
