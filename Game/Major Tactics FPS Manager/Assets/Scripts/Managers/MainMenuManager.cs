using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor.UI;

public class MainMenuManager : MonoBehaviour
{
    private GameObject activeButton = null;
    private float buttonAnimationSpeed;
    private int buttonAnimationCounter = 0;
    private int buttonAnimationLength = 100;

    public GameObject[] Panels;
    private int activePanel = 0;

    private void Start()
    {
        buttonAnimationSpeed = GameObject.Find("MainMenuCanvas").GetComponent<RectTransform>().rect.width/ buttonAnimationLength *2;
    }

    public void onButtonClick(string buttonName)
    {
        activeButton = GameObject.Find(buttonName);
        activeButton.transform.SetAsLastSibling();
    }
    
    public void BackButton(int i) {
        Panels[i].SetActive(false);
        Panels[0].SetActive(true);
        activePanel = 0;
    }

    private void Update()
    {
        if (activeButton != null)
        {
            activeButton.GetComponent<RectTransform>().sizeDelta += new Vector2(buttonAnimationSpeed, 0f);
            if (buttonAnimationCounter > buttonAnimationLength)
            {
                ButtonExecution();
                buttonAnimationCounter = 0;
                activeButton.GetComponent<RectTransform>().sizeDelta = new Vector2(0f, 0f);
                activeButton = null;
            }
            else
            {
                buttonAnimationCounter++;
            }
        }
    }

    private void CloseActivePanel()
    {
        Panels[activePanel].SetActive(false);
    }

    private void ButtonExecution()
    {
        CloseActivePanel();
        switch (activeButton.name)
        {
            case "PlayButton":
                activePanel = 1;
                break;
            case "TeamButton":
                activePanel = 2;
                break;
            case "CalendarButton":
                activePanel = 3;
                break;
            case "StandingButton":
                activePanel = 4;
                break;
            case "TradeButton":
                activePanel = 5;
                break;
            case "SettingsButton":
                activePanel = 6;
                break;
            default:
                activePanel = 0;
                break;
        }
        Panels[activePanel].SetActive(true);
    }


}
