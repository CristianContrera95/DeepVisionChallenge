# DeevVisionChallenge  

You must have **Docker** installed  
You can also change the docker name on the first line of **run.sh** (defaul: cristiancontrera)

Once the project is downloaded, run (without fear):  
```
./run.sh *images_input_date* *overlap thresh*  
```

example:
```
./run.sh images_data/ 0.4  
```

Note: If you want to test the nms function, you can import it and call it with array of *boxes* and *overlap thresh* parameters
