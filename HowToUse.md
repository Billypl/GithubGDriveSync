# How to 

## Tutorial - mixed CLI and GitHub page
Quick forking tutorial for newbies: https://www.youtube.com/watch?v=CML6vfKjQss

## Tutorial - CLI only:
```bash
# install CLI GitHub and Git (gh and git packages)
sudo apt install git
sudo apt install gh
gh auth login

# fork the repo
gh repo fork REPO_OWNER_USERNAME/REPO_NAME --clone
cd REPO_NAME/shared
git checkout -b YOUR_BRANCH_NAME

# add your files here
git add .
git commit -m "YOUR_MESSAGE_HERE"
# when you want to push changes to your forked repo:
# for the first time
git push -u origin YOUR_BRANCHNAME
# any other time
git push

# when you want to merge changes to original repo
gh pr create --base master --head YOUR_USERNAME:YOUR_BRANCH_NAME --repo Billypl/PaczkownicyInfaPG
```