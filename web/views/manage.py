import json
from . import app
from os import getenv as _
from utils import md5, validjson
from models import Tag, Video, VideoTag
from playhouse.shortcuts import model_to_dict
from playhouse.flask_utils import PaginatedQuery
from middleware import mng_combined, api_response
from flask import request, redirect, make_response, render_template


@app.route('/tag', methods=['GET', 'POST'])
@app.route('/tag/<id>', methods=['GET', 'POST'])
@mng_combined
def tag(id=0):
    if request.method == 'POST':
        return Tag.edit(id, name=request.form.get('name'))

    tag = Tag.get_by_id(id)
    return render_template('tag.html', tag=tag)


@app.route('/tags')
@mng_combined
def tags():
    if 'q' in request.args:
        q = f'%{request.args["q"]}%'
        return 1, [model_to_dict(tag) for tag in Tag.select().where(Tag.name ** q).limit(10)]

    if 'list' in request.args:
        pagination = PaginatedQuery(Tag.select().order_by(Tag.id.desc()), 50)
        return 1, {
            'pre': 50,
            'page': pagination.get_page(),
            'count': Tag.select().count(),
            'data': [model_to_dict(video) for video in pagination.get_object_list()]
        }

    return render_template('tags.html')


@app.route('/video', methods=['GET', 'POST'])
@app.route('/video/<id>', methods=['GET', 'POST'])
@mng_combined
def video(id=0):
    if 'remove' in request.form:
        return Video.remove(id)

    video = Video.get_by_id(id) if id else {}
    return render_template('video.html', video=video)


@app.route('/videos')
@mng_combined
def videos():
    if 'tag' in request.args:
        return 1, VideoTag.blend(request.args['tag'])

    return render_template('videos.html')


@app.route('/offline', methods=['GET'])
@mng_combined
def offline(id=0):
    return render_template('offline.html')


@app.route('/tag_videos', methods=['GET', 'POST'])
@app.route('/tag_videos/<id>', methods=['GET', 'POST'])
@mng_combined
def tag_videos(id=0):
    if 'videos' in request.form:
        if not validjson(request.form['videos']):
            return 0, 'Videos parame is not a valid JSON'

        return VideoTag.save_videos(id, json.loads(request.form['videos']))

    return render_template('videos.html')


@app.route('/login', methods=['GET', 'POST'])
@api_response
def login():
    if 'auth' in request.args:
        if request.args['auth'] != md5(_('SECRET')):
            return 0, '无效的 Token'

        resp = make_response(redirect(request.args.get('goto')))
        resp.set_cookie('secret', _('SECRET'))
        return resp

    if 'secret' in request.form:
        secret = request.form['secret']
        if not _('SECRET') == secret:
            return 0, '登录失败'

        resp = make_response('[1, "OK"]')
        resp.set_cookie('secret', secret)
        return resp

    resp = make_response(render_template('login.html'))
    resp.delete_cookie('secret')
    return resp
