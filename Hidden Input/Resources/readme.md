# Hidden Input

The `<input type="hidden">` defines a hidden input field. We can find it in lot of pages in the website. But the one we're talking about here is when you go to `sign in` and click `forget password`

![alt text](img/forget_password.png "Forget Password")

It's weird to have a forget password and not have email input. So we viewed the source page. In the source you will find a `<input type="hidden" ...>`.

![alt text](img/page_source.png "Source Page")

Let's go back to our page, and use `web developer tool` so we can change it.

![alt text](img/inspect_element.png "Inspect Element")

Then we submit and we can get the flag.

![alt text](img/flag.png "Flag")

## How to protect ?
Don't use hidden input or if you use it, add readonly attribute.
