from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball": League.objects.filter(sport__contains="baseball"),
		"women": League.objects.filter(name__contains="Women"),
		"hockey": League.objects.filter(sport__contains="hockey"),
		"football": League.objects.exclude(sport__contains="football"),
		"conferences": League.objects.filter(name__contains="Conference"),
		"atlantic": League.objects.filter(name__contains="Atlantic"),
		"dallas": Team.objects.filter(location__contains="Dallas"),
		"raptors": Team.objects.filter(team_name__contains="Raptors"),
		"city": Team.objects.filter(location__contains="City"),
		"t": Team.objects.filter(team_name__startswith="T"),
		# "abc": Team.objects.order_by(team_name),

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")