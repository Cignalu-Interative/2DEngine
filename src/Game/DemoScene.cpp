#include "pch.h"
#include "DemoScene.h"

#include "2DPendentLib/InputManager.h"
#include "2DPendentLib/AssetManager.h"
#include "2DPendentEngine/MapTiledManager.h"
#include "2DPendentLib/FontManager.h"

#include <iostream>

inline Debug& debug = *Debug::Get();
inline InputManager& input = *InputManager::Get();
inline SoundManager& sound = *SoundManager::Get();

DemoScene::DemoScene()
{

}

void DemoScene::OnInitialize()
{
	AssetManager::Get()->AddTextureByRepertory("../../res/Game/Assets/Textures/Textures_Repertory.json");
	MapTiledManager::Get()->AddMaps("../../res/2DPendentEngine/Assets/Maps/Maps_Repertory.json");
	SoundManager::Get()->AddSound("../../res/2DPendentEngine/Assets/Sounds/Sounds_Repertory.json");
	FontManager::Get()->AddFontByRepertory("../../res/2DPendentEngine/Assets/Fonts/Fonts_Repertory.json");


}

void DemoScene::OnEvent()
{
	
}

void DemoScene::OnUpdate()
{

}

void DemoScene::OnSleep()
{
	SetIsVisible(false);
	SetSleepEvent(true);
	SetSleepUpdate(true);
}

void DemoScene::OnWake()
{
	SetIsVisible(true);
	SetSleepEvent(false);
	SetSleepUpdate(false);
}

void DemoScene::OnDestroy()
{
	debug.ClearAll();
	GetEntities().clear();
}

void DemoScene::OnDraw()
{
}

