using UnityEngine;

public class WallMove : MonoBehaviour
{
    public float moveSpeed;

    private Vector3 oldPosition;
    private GameObject obj;

    // Start is called before the first frame update
    void Start()
    {
        obj = gameObject;
        oldPosition = obj.transform.position;
        moveSpeed = 5;
    }

    // Update is called once per frame
    void Update()
    {
        obj.transform.Translate(new Vector3(-1 * Time.deltaTime * moveSpeed, 0, 0));
    }
}
