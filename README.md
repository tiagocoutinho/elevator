# Elevator

Solve elevator problem from Dinesman 1968 in python.

Each commit whoose message starts with `vX:` is a new version (suposably faster than the previous).

<table>
  <thead>
    <tr>
      <th>Version</th>
      <th>Description</th>
      <th>Time</th>
      <th>Speedup (from v1)</th>
      <th width="400px">Graph</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/tiagocoutinho/elevator/tree/df742e0">v4</a></td>
      <td>Preemptively exit loop</td>
      <td>534 ns ± 38.7 ns</td>
      <td>541x</td>
      <td><div style="background-color:blue; width: 1px;">&nbsp;</div></td>
    </tr>
    <tr>
      <td><a href="https://github.com/tiagocoutinho/elevator/tree/a00b30c">v3</a></td>
      <td>Basic reduce loop</td>
      <td>6.15 μs ± 36.9 ns</td>
      <td>47x</td>
      <td><div style="background-color:orange; width: 9px;">&nbsp;</div></td>
    </tr>
    <tr>
      <td><a href="https://github.com/tiagocoutinho/elevator/tree/82bad78">v2</a></td>
      <td>Reorder loops</td>
      <td>36.6 μs ± 276 ns</td>
      <td>8x</td>
      <td><div style="background-color:red; width: 51px;">&nbsp;</div></td>
    </tr>
    <tr>
      <td><a href="https://github.com/tiagocoutinho/elevator/tree/82bad78">v1</a></td>
      <td>Naive approach</td>
      <td>289 μs ± 1.25 μs</td>
      <td>1x</td>
      <td><div style="background-color:magenta; width: 400px;">&nbsp;</div></td>
    </tr>
  </tbody>
</table>
