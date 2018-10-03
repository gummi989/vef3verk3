<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>The Best News</title>
    <link rel="stylesheet" href="/static/news.css">
</head>
<body>
    % include("header.tpl")
    <div class="row">
        <section><h2>Title</h2></section>
        <section><h2>Latest stories</h2></section>
        <section><img src="/static/shrek.jpg" alt="Shrek"></section>
        <section>
            <ul>
                % for i, story in enumerate(stories):
                    <li><a href="/b/story/{{i}}">{{story[0]}}</a></li>
                % end
            </ul>
        </section>
    </div>
    % include("footer.tpl")
</body>
</html>