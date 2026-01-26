The main goal of this version is to make able to deliver a production ready version of the multiverse. The idea is that if I am a rookie bioinformatician who wants to try to use the multiverse tool, what is the minimal number of steps I should do to get a running version?

Here I detail **a simple user workflow**:

1. I clone the repo
2. I setup a virtual env for running the repo
    1. requires docker
    2. asks for which models to build their dockers images first
    3. asks for a location where data should be read from and stored
    4. my dataset should have a given config file detailing which omics is inside and what is my file format and cell type / batch label exist (if any)
        1. I receive an error if such file doesnt exist
3. After the setup is done, I can now run the main runner where I ask for data integration of my dataset that I point to its location, and which models to use from
    1. I should not worry about which models I am allowed to use, I want the multiverse to pick from my selection the only suitable ones (@rishi, mind you not all models work for all types of omics, some work for RNA and ATAC only, while others are more generic like pca)
4. As the algorithm is working, I would like to keep getting progress detailing the progress of the models, and where their metadata is saved
5. Once the models are done, I see that the evaluation module is running and the results are saved. I see the results are saved in a json in the save directory

I also provide you with an **updated list of requirements** to be added by priority:

- spin the different docker images in parallel, not sequentially
- update the make file
- build all needed images in the beginning
- make the image names mapping outside the docker runner class
- adding rules for which datasets can work with which models
- model finishing sucessfully or not
- update readme file - maybe combine it with docs ??
- fix datasets async or not once before all models
- add key for batch and cell type in config file
- unit tests?
- add seeds for all models
- make a gui
- freeze libraries and set all them to updated versions or what library asks for
- what if there is no cell type or one batch only?
- control which metrics to run