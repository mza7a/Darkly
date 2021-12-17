# Survey Exploit

On the home page of our website and on the right, we find a tab named `survey`. We click on it

![alt text](img/survey_tab.png "Survey Tab")

![alt text](img/survey_page.png "Survey Page")

Let's inspect the `Grade` for `Laurie`.

![alt text](img/inspec_survey.png "Inspect Survey")

Now we can change the value of for example `10` to something like this `100000`...

![alt text](img/change_value.png "Changing Value")

We can then chose it back in the website, and we have the flag.

![alt text](img/flag.png "Flag")

## How to protect ?
Here we can just do a comparaison to whatever the user has entered in the value, for this example `1 <= x <= 10`. So even if a hecker changes the value, it will not be sumbited due the unequal sentence.