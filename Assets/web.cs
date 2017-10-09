using UnityEngine;
using UnityEngine.Networking;
using System.Collections;
using System.Collections.Generic;

public class web : MonoBehaviour
{


    public string host= "http://127.0.0.1:5000/";
    void Start()
    {
        //host = "http://127.0.0.1:5000/";
        StartCoroutine(Upload());
        StartCoroutine(joinGame());

    }

    IEnumerator Upload()
    {
        List<IMultipartFormSection> formData = new List<IMultipartFormSection>();
        formData.Add(new MultipartFormDataSection("id=70"));
        //formData.Add(new MultipartFormFileSection("my file data", "myfile.txt"));

        WWW www = new WWW(host+"signUpUser?id=70");
        yield return www;

        if (www.error != null)
        {
            Debug.Log(www.error);
        }
        else
        {

            Debug.Log(www.text);

        }
    }
    IEnumerator joinGame()
    {

        //formData.Add(new MultipartFormDataSection("id=70"));
        //formData.Add(new MultipartFormFileSection("my file data", "myfile.txt"));

        WWW www = new WWW(host+"joingame?min%20players=0&id=70");
        yield return www;

        if (www.error != null)
        {
            Debug.Log(www.error);
        }
        else
        {

            Debug.Log(www.text);

        }

    }
}