using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SplashScreenManager : MonoBehaviour
{
    // After the scene loads wait a few seconds before loading MainMenu scene
    void Start() => StartCoroutine(WaitTime(3));

    IEnumerator WaitTime(int seconds)
    {
        yield return new WaitForSeconds(seconds);
        SceneManager.LoadScene("MainMenu", LoadSceneMode.Single);
    }
}
