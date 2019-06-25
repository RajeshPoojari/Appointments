"""from sqlalchemy.sql import func
qry = session.query(func.max(Score.score).label("max_score"), 
                    func.sum(Score.score).label("total_score"),
                    )
qry = qry.group_by(Score.name)
for _res in qry.all():
    print _res"""