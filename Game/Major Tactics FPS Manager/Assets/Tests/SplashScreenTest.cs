using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using UnityEngine.UI;

public class SplashScreenTest
{

    [Test]
    public void SplashScreenTestSplash_ScreenImageExists()
    {
        // Testing to see if the Splash screen image has been loaded
        Assert.AreNotEqual(GameObject.Find("SplashScreenImage").GetComponent<Image>().sprite, null);
    }
}
