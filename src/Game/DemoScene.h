#pragma once
#include "2DPendentEngine/Scene.h"
#include <list>
#include <vector>

class DemoScene : public Scene
{
private:


protected:

	//Fonctions virtuelles héritées de Scene pour définir la logique d'initialisation, de gestion des événements, de mise à jour et de destruction de la scène
	void OnInitialize() override;
	//Fonction pour gérer les événements liés à la scène, notamment en utilisant l'InputManager pour détecter les entrées utilisateur spécifiques à cette scène
	void OnEvent() override;
	//Fonction pour mettre à jour la logique de la scène, notamment en mettant à jour les joueurs et les autres éléments présents dans la scène
	void OnUpdate() override;
	//Fonction virtuelle pure pour permettre aux classes qui héritent de Scene de définir leur propre logique de mise en veille
	void OnSleep() override;
	//Fonction virtuelle pure pour permettre aux classes qui héritent de Scene de définir leur propre logique de réveil
	void OnWake() override;
	//Fonction pour libérer les ressources utilisées par la scène, notamment en détruisant les joueurs et les autres éléments présents dans la scène
	void OnDestroy() override;
	void OnDraw() override;

public:

	DemoScene();
	~DemoScene() = default;
};