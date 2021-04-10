using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using UnityEngine.UI;

public class MainMenuTests
{
    [Test]
    public void MainMenuTests_LogoExists()
    {
        // Check if the logo image exists
        Assert.AreNotEqual(GameObject.Find("YourTeamLogo").GetComponent<Image>().sprite, null);
    }

    [Test]
    public void MainMenuTests_TeamNameFieldExists()
    {
        // Check if the team name exists
        Assert.AreNotEqual(GameObject.Find("TeamNameText"), null);
    }

    [Test]
    public void MainMenuTests_ManagerNameFieldExists()
    {
        // Check if the manager name exists
        Assert.AreNotEqual(GameObject.Find("ManagerNameText"), null);
    }

    [Test]
    public void MainMenuTests_MoneyAreaExists()
    {
        // Check if the money indicator exists
        Assert.AreNotEqual(GameObject.Find("MoneyInfo"), null);
        Assert.AreNotEqual(GameObject.Find("MoneyImage"), null);
        Assert.AreNotEqual(GameObject.Find("MoneyAmount"), null);
    }

    [Test]
    public void MainMenuTests_TokenAreaExists()
    {
        // Check if the token indicator exists
        Assert.AreNotEqual(GameObject.Find("TokenInfo"), null);
        Assert.AreNotEqual(GameObject.Find("TokenImage"), null);
        Assert.AreNotEqual(GameObject.Find("TokenAmount"), null);
    }

    [Test]
    public void MainMenuTests_FansAreaExists()
    {
        // Check if the fans indicator exists
        Assert.AreNotEqual(GameObject.Find("FansInfo"), null);
        Assert.AreNotEqual(GameObject.Find("FanImage"), null);
        Assert.AreNotEqual(GameObject.Find("FanAmount"), null);
    }
}
