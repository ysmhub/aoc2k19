<?php

$fuel = 0;
while($mass = intval(fgets(STDIN)) ) $fuel += floor($mass/3) - 2;
echo "$fuel\n";

