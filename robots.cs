Function (1)
// Moves forward then on obstacle detection reverse for 2 seconde
void MoveForwardSimple()
 {
  if (CentreSensor || RightSensor || LeftSensor)
     {
      backTimestamp = Time.time +2f;
     }
  if (BackTimestamp > Time.time)
     {
      TheV = -0.5f;
     }
  else 
     {
      TheV = 1;
     }
 }



// Variable for Cube pick function, cone pick function and drive target function
float ObstacleTimestamp;
float WaitTimestamp;
float PlacedTimestamp;
float Taketimestamp;
float CheckMoveTimestamp;
public float Opposite = 1;
float ImmobileTimestamp;
float ReverseTimestamp;



Function (2)
// Move To SaveZone on Siren enable
 void SirenMove()
   {
     if (SirenOn ==  true)
       {
        DriveToTarget(SaveZonePoint);
       }
   }



Function (3)
//Logic for basic gameplay functions
 void Logic()
 {
  if (ClosestCube != null && Vector3.Distance(MyRobot.transform.position, ClosestCube.postion >3)
   {
    ClosestCube = null;
   }
  if (ClosestCone != null && Vector3.Distance(MyRobot.transform.position, ClosestCone.postion >3)
   {
    ClosestCone = null;
   }
  if (TakeTimestamp < Time.time)
   {
       if (ClosestCone == null)
        {
         ClosestCone = GetClosest(TheCones);
        }
       if (ClosestCube == null)
        {
         ClosestCube = GetClosest(TheCubes);
        }
    TakeTimestamp = Time.time + 1;
   }
 }
 void AssignCubeOwner(GameObject TheCube)
   {
     CubeAsign = TheCube;
   }   
 void AssignConeOwner(GameObject TheCone)
   {
     CubeAsign = TheCone;
   } 



Function (4)
 public void TakeCube()
  {
   if (PlacedTimestamp > Time.time)
     {
      retun;
     }
   if (ClosestCube != null)
     {
       if (ClosestCube.GetComponent<Rigidbody>().isKinematic)
         {
           ClosestCube = null;
         }
       if (vector3.Distance(ClosestCube.position, MyRobot.transform.postion) < 1)
         {
          AssignCubeOwner(ClosestCube.gameObject);
          ClosestCube.transform.position = PickPosition.transform.postion;
          ClosestCube.transform.rotation = PickPosition.transform.rotation;
          ClosestCubeDest = GetClosest(TheCubesDest);
          DriveToTarget(ClosestCubeDest);
            if (Vector3.Distance(MyRobot.transform.postion, ClosestCubeDest.position) < 1)
              {
                ClosestCube.position = ClosestCubeDest.position;
                ClosestCube.rotation = ClosestCubeDest.rotation;
                PlacedTimestamp = Time.time + 2f;
              }
               return;
         }
          DriveToTarget(ClosestCube);
     }
  }



Function (5)
 public void TakeCone()
   {
     if (PlacedTimestamp > Time.time)
         {
           return;
         }
     if (ClosestCone != null
        {
          if (ClosestCone.GetComponent<Rigidbody>().isKinematic)
             {
               ClosestCone = null;
             }
           if (vector3.Distance(ClosestCone.position, MyRobot.transform.postion) < 1)
         {
          AssignConeOwner(ClosestCone.gameObject);
          ClosestCone.transform.position = PickPosition.transform.postion;
          ClosestCone.transform.rotation = PickPosition.transform.rotation;
          ClosestConeDest = GetClosest(TheConesDest);
          DriveToTarget(ClosestConeDest);
            if (Vector3.Distance(MyRobot.transform.postion, ClosestConeDest.position) < 2)
              {
                ClosestCone.position = ClosestConeDest.position;
                ClosestCone.rotation = ClosestConeDest.rotation;
                PlacedTimestamp = Time.time + 2f;
              }
           return;
         }
          DriveToTarget(ClosestCone);
     }
  }




Function (6)
  void DriveToTarget(Transform TheTarget)
     {
       HolderSteerHelper.LookAt(TheTarget);
       float YAngle = HolderSteerHelper.eulerAngles.y;
       SteerHelper.eulerAngles = new Vector3(MyRobot.transform.eulerAngles.x, YAngle, MyRobot.transform.eulerAngles.z);
       float AngleDif = Mathf.DeltaAngle(SteerHelper.eulerAngles.y, MyRobot.transform.eulerAnles.y);
       if (ObstacleTimestamp > Time.time)
          {
            WaitTimestamp = Time.time + 2;
            return;
          }
      if (RightSensor && !LeftSensor && !CentreSensor)
         {
           TheX = -0.2f * Opposite;
           TheV = 0.5f * opposite;
           if (WaitTimestamp < Time.time)
              {
                ObstacleTimestamp = Time.time + 2;
              }
         }
       else if (LeftSensor && !RightSensor && !CentreSensor)
         {
            TheX = 0.2f * Opposite;
            TheV = 0.5f * opposite;
            if (WaitTimestamp < Time.time)
              {
                ObstacleTimestamp = Time.time + 2;
              }
         } 
        else if (LeftSensor && RightSensor && CentreSensor)
         {
            TheX = 0;
            TheV = -0.5f * opposite;
            if (WaitTimestamp < Time.time)
              {
                ObstacleTimestamp = Time.time + 2;
              }
         }  
        else
         {
           if (AngleDif < 45 && AngleDif > -45)
              {
                TheX = (-AngleDif / 45) * Opposite;
                TheV = 0.5f * Opposite;
              }
           else
             {
                if (AngleDif > 45)
                  {
                    TheX = 1 * Opposite;
                  }
                 else
                    {
                       if (AngleDif < -45)
                         {
                           TheX = -1 * Opposite; 
                          }
                       if (BackCentreSensor)
                          {
                            TheX = 0.5f * Opposite;
                            TheV = 1 * Opposoite;
                          }
                  else 
                      {
                        TheV = -0.5f * Opposite;
                        if (ReverseTimestamp < Time.time)
                           {
                             
                           }
                        else
                           {
                           }
                      }
                    }  
              }  
            if (MyRobot.GetComponent<Rigidbody>().velocity.magnetude < 0.1f)
                {
                  ImmobileTimestamp += Time.deltaTime;
                  if (ImmobileTimestamp > 1 && CheckMoveTimestamp < Time.time)
                     {
                       Opposite = -Opposite;
                       if (Opposite < 0)
                          {
                            Opposite = -0.2f;
                          }
                       else
                          {
                            Opposite = 1;
                          }
                       CheckMoveTimestamp = Time.time + ImmobileTimestamp;
                     }
                } 
              else
                {
                  if (Time.time > CheckMoveTimestamp)
                     {
                       ImmobileTimestamp = 0;
                       Opposite = 1;
                     }
                }   
         }     




Function (7)
//Get the closest object from a given list
   Transform GetClosest(List<Transform> TheObjs)
   {
    float[]TheDist = new float[TheObjs.Count];
    float MaxDist = 3;
    for (int i = 0; i < TheObjs.Count; i++)
        {
          if (TheObjs[i] != null)
             {
              TheDist[i] = Vector3.Distance(PickPostion.transform.position, TheObjs[i].position);
             }
          else
             {
              TheObjs.RemoveAt(i);
             }
        }
     float[] Sorted = (float[])Thedist.Clone();
     Array.Sort(Sorted);
     for (int t = 0; t < TheDist.Length; t++)
      {
       if (Sorted[0] == TheDist[t])
          {
           return TheObjs[t];
          }
      }
      return null;
   }