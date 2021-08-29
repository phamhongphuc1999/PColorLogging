using UnityEngine;

public class BirdController : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnCollisionEnter2D(Collision2D other)
    {
        Debug.Log("EndGame");
    }

    void OnCollisionStay()
    {

    }

    void OnCollisionExit()
    {

    }

    void OnTriggerEnter()
    {

    }

    void OnTriggerStay()
    {

    }

    void OnTriggerExit()
    {

    }
}
