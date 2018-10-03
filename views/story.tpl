<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>{{story[0]}} - The Best News</title>
    <link rel="stylesheet" href="/static/news.css">
</head>
<body>
    % include("header.tpl")
    <div class="row">
        <section><h2>{{story[0]}}</h2></section>
        <section><!-- Empty section --></section>
        <section>
            <img src="/static/story-{{id}}.jpg" alt="{{story[0]}}">
        </section>
        <article>
            <p>{{story[1]}}</p>
            <small>{{story[2]}}</small>
            <a class="back-btn" href="/b">Back</a>
        </article>
    </div>
    % include("footer.tpl")
</body>
</html>
