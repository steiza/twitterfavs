<html>
    <head>
        <link href='/static/css/style.css' type='text/css' rel='stylesheet' />
        <script type='text/javascript' src='static/js/jquery-1.6.2.min.js'></script>
    </head>
    <body>
        <div class='loading_frame'>
            <div class='loading'>
                <p>Searching the Internet for nice comments...</p>
                <p>... may take a while</p>
            </div>
        </div>
        <ul>
        % for each in content:
            <li class='testimonial_frame'>
                <div class='tweet_header'>
                    <a href='https://twitter.com/${each['user']['screen_name']}'>
                        <img class='twitter_pic' src=${each['user']['profile_image_url']}>
                        <span class='name'>
                            ${each['user']['name']}
                        </span>
                        <span class='twitter_username'>
                            @${each['user']['screen_name']}
                        </span>
                    </a>
                    <a href='https://twitter.com/coffeehousecode/status/${each['id_str']}'>
                        <span class='date'>
                            ${' '.join(each['created_at'].split(' ')[1:3])}
                        </span>
                    </a>
                </div>
                <p class='tweet_text'>
                    <a href='https://twitter.com/coffeehousecode/status/${each['id_str']}'>
                        ${each['text']}
                    </a>
                </p>
            </li>
        % endfor
        </ul>
        <script type='text/javascript'>
            $(window).load(function() {
                    $('.loading_frame').hide();
                    $('.testimonial_frame').fadeIn(2000);
            });
        </script>
    </body>
</html>
