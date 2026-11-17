# RoboHeads Playground

Practice repo for the first RoboHeads training (Git + GitHub). Nothing here matters, break things freely.

## Exercise

1. **Fork** this repo (button top right).
2. Clone **your fork**: `git clone https://github.com/<your-username>/roboheads-playground.git`
3. `cd roboheads-playground`
4. `git switch -c <your-name>`
5. Create `people/<your-name>.md` with one sentence about yourself.
6. `git add people/<your-name>.md`
7. `git commit -m "Add <your-name>"`
8. `git push -u origin <your-name>`
9. On GitHub, open a **Pull Request** from your branch to `Roboheads/roboheads-playground` `main`.

Use `git status` after every step.

## ROS 2 + Gazebo + RViz (dev container)

You only need Docker Desktop and VS Code with the Dev Containers extension. Same steps on Windows, Mac and Linux.

1. Open the repo in VS Code and choose **Reopen in Container** (first build takes a few minutes).
2. Open <http://localhost:6080> in your browser and click **Connect**. Password: `vscode`. This is the container's desktop.
3. In the VS Code terminal (inside the container) run `rviz2`, or the TurtleBot3 launch. The windows appear in the browser desktop.

Rendering is on the CPU, so Gazebo can be slow. That is expected.
