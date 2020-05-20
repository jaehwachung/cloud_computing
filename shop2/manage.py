#!/usr/bin/env python
import click
import json
from flask import Flask
from flask.cli import FlaskGroup
from models import ShopMember, Goods
from sqlalchemy import func
from database import db_session

def create_app():
    from shop_main import app
    return app

@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Management script for the Wiki application."""

@cli.command()
def create_db():
    from database import init_db

    init_db()

    click.echo("DB 스키마가 생성되었습니다")

@cli.command()
def user_create():
    """User Create"""
    admin_user = ShopMember()
    admin_user.name = '관리자'
    admin_user.email = 'admin@easymall.kr'
    admin_user.password = '1234'
    admin_user.is_admin = 'Y'
    admin_user.create_date = func.now()

    db_session.add(admin_user)
    db_session.commit()
    
@cli.command()
def goods_insert():
    """Goods Insert"""

    products = (
        ('제품1', 30000, 'wenyang-x700.jpg', 10, 3, '제품1에 대한 설명이 여기에 들어옵니다'),
        ('제품2', 33000, 'tamara-bellis-x700.jpg', 10, 5, '제품2에 대한 설명이 여기에 들어옵니다'),
        ('제품3', 35000, 'roland-denes-x700.jpg', 10, 1, '제품3에 대한 설명이 여기에 들어옵니다'),
        ('제품4', 33000, 'raamin-ka-x700.jpg', 10, 2, '제품4에 대한 설명이 여기에 들어옵니다'),
        ('제품5', 31000, 'oliver-johnson-x700.jpg', 10, 5, '제품5에 대한 설명이 여기에 들어옵니다'),
        ('제품6', 36000, 'taisiia-stupak-x700.jpg', 10, 4, '제품6에 대한 설명이 여기에 들어옵니다')
    )

    for item in products:
        goods = Goods()
        goods.goods_name = item[0]
        goods.price = item[1]
        goods.goods_photo = item[2]
        goods.goods_cnt = item[3]
        goods.goods_ranking = item[4]
        goods.goods_description = item[5]

        db_session.add(goods)
    
    db_session.commit()

@cli.command()
@click.option('--host', default="", help='DB Host')
@click.option('--user', default="", help='DB User')
@click.option('--password', default="", help='DB User Password')
@click.option('--db', default="", help='DB Name')
def db_info(host, user, password, db):
    json.dump({
        "host": host,
        "user": user,
        "password": password,
        "database": db
    }, open("/opt/knou/shop2/database.json", "w"))
    
    click.echo("데이터베이스 정보가 잘 생성되었습니다")


if __name__ == '__main__':
    cli()
