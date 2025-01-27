
def init():
    import juliapkg
    from juliacall import Main as jl
    # print("Setting up julia installation and packages...")
    juliapkg.require_julia("1.10")
    juliapkg.add("BayesianSurvival", "397a51c9-aa1e-4c06-9799-c451da7f7981", url="https://github.com/nsiccha/BayesianSurvival.jl.git")
    juliapkg.add("Mooncake", "da2b9cff-9c12-43a0-ae48-6db2b0edb7d6")
    juliapkg.add("DynamicHMC", "bbc10e6e-7c05-544b-b16e-64fede858acb")
    juliapkg.add("StatsPlots", "f3b207a7-027a-5e70-b257-86293d7955fd")
    juliapkg.resolve()
    # print("Importing required julia packages...")
    jl.seval("using BayesianSurvival, DynamicHMC, Mooncake, StatsPlots")
    # print("Done setting up julia.")
    return jl