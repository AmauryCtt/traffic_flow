from traffic import traffic_network

def print_flow(flow_value, flow_dict, title):
    print(f"\n{title}")
    print(f"Débit maximal : {flow_value}00 véhicules/heure")
    print("\nRépartition du flux :")
    for u in sorted(flow_dict):
        for v in sorted(flow_dict[u]):
            if flow_dict[u][v] > 0:
                print(f"  {u:5} -> {v:5} : {flow_dict[u][v]:2}00 véhicules/heure")


def run_question_1():
    print("="*40)
    print("Question 1 : Sans contraintes sur les villes")
    print("="*40)
    flow_value, flow_dict = traffic_network.max_vehicule()
    print_flow(flow_value, flow_dict, "Flux sans contraintes ville")


def run_question_2et3():
    print("\n" + "="*40)
    print("Question 3 : Avec contraintes sur les villes")
    print("="*40)
    flow_value, flow_dict = traffic_network.max_vehicule_avec_flux()
    print_flow(flow_value, flow_dict, "Flux avec contraintes ville")


def run_question_4():
    print("\n" + "="*40)
    print("Question 4 : Variation du débit en fonction de la capacité de la ville d")
    print("="*40)
    resultats = traffic_network.variation_d()

    print("\nCapacité de d | Débit maximal")
    print("-----------------------------")
    for cap, flow in resultats.items():
        print(f"{cap:<14} | {flow}00 véhicules/heure")


def main():
    print("\n=== Analyse complète du réseau routier ===")
    run_question_1()
    run_question_2et3()
    run_question_4()
    print("\n Analyse terminée.")


if __name__ == "__main__":
    main()
