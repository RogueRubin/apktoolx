.class public Lxyz/NoSignApplication;
.super Landroid/app/Application;
.source "NoSignApplication.java"

# interfaces
.implements Ljava/lang/reflect/InvocationHandler;


# static fields
.field private static final GET_SIGNATURES:I = 0x40


# instance fields
.field private appPkgName:Ljava/lang/String;

.field private base:Ljava/lang/Object;

.field private sign:[[B


# direct methods
.method public constructor <init>()V
    .registers 2

    .prologue
    .line 16
    invoke-direct {p0}, Landroid/app/Application;-><init>()V

    .line 18
    const-string v0, ""

    iput-object v0, p0, Lxyz/NoSignApplication;->appPkgName:Ljava/lang/String;

    return-void
.end method

.method private hook(Landroid/content/Context;)V
    .registers 22
    .param p1, "context"    # Landroid/content/Context;
    .annotation build Landroid/annotation/TargetApi;
        value = 0x8
    .end annotation

    .prologue
    .line 25
    const/16 v17, 0x1

    :try_start_2
    move/from16 v0, v17

    new-array v3, v0, [[B

    const/16 v17, 0x0

    const-string v18, "### Signatures Data ###"

    const/16 v19, 0x0

    invoke-static/range {v18 .. v19}, Landroid/util/Base64;->decode(Ljava/lang/String;I)[B

    move-result-object v18

    aput-object v18, v3, v17

    .line 26
    .local v3, "bArr":[[B
    const-string v17, "android.app.ActivityThread"

    invoke-static/range {v17 .. v17}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v4

    .line 27
    .local v4, "cls":Ljava/lang/Class;
    const-string v17, "currentActivityThread"

    const/16 v18, 0x0

    move/from16 v0, v18

    new-array v0, v0, [Ljava/lang/Class;

    move-object/from16 v18, v0

    move-object/from16 v0, v17

    move-object/from16 v1, v18

    invoke-virtual {v4, v0, v1}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v17

    const/16 v18, 0x0

    const/16 v19, 0x0

    move/from16 v0, v19

    new-array v0, v0, [Ljava/lang/Object;

    move-object/from16 v19, v0

    invoke-virtual/range {v17 .. v19}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v12

    .line 28
    .local v12, "invoke":Ljava/lang/Object;
    const-string v17, "sPackageManager"

    move-object/from16 v0, v17

    invoke-virtual {v4, v0}, Ljava/lang/Class;->getDeclaredField(Ljava/lang/String;)Ljava/lang/reflect/Field;

    move-result-object v7

    .line 29
    .local v7, "declaredField":Ljava/lang/reflect/Field;
    const/16 v17, 0x1

    move/from16 v0, v17

    invoke-virtual {v7, v0}, Ljava/lang/reflect/Field;->setAccessible(Z)V

    .line 30
    invoke-virtual {v7, v12}, Ljava/lang/reflect/Field;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v15

    .line 31
    .local v15, "obj":Ljava/lang/Object;
    const-string v17, "android.content.pm.IPackageManager"

    invoke-static/range {v17 .. v17}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v5

    .line 32
    .local v5, "cls2":Ljava/lang/Class;
    move-object/from16 v0, p0

    iput-object v15, v0, Lxyz/NoSignApplication;->base:Ljava/lang/Object;

    .line 33
    move-object/from16 v0, p0

    iput-object v3, v0, Lxyz/NoSignApplication;->sign:[[B

    .line 34
    invoke-virtual/range {p1 .. p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v17

    move-object/from16 v0, v17

    move-object/from16 v1, p0

    iput-object v0, v1, Lxyz/NoSignApplication;->appPkgName:Ljava/lang/String;

    .line 35
    invoke-virtual {v5}, Ljava/lang/Class;->getClassLoader()Ljava/lang/ClassLoader;

    move-result-object v17

    const/16 v18, 0x1

    move/from16 v0, v18

    new-array v0, v0, [Ljava/lang/Class;

    move-object/from16 v18, v0

    const/16 v19, 0x0

    aput-object v5, v18, v19

    move-object/from16 v0, v17

    move-object/from16 v1, v18

    move-object/from16 v2, p0

    invoke-static {v0, v1, v2}, Ljava/lang/reflect/Proxy;->newProxyInstance(Ljava/lang/ClassLoader;[Ljava/lang/Class;Ljava/lang/reflect/InvocationHandler;)Ljava/lang/Object;

    move-result-object v14

    .line 36
    .local v14, "newProxyInstance":Ljava/lang/Object;
    invoke-virtual {v7, v12, v14}, Ljava/lang/reflect/Field;->set(Ljava/lang/Object;Ljava/lang/Object;)V

    .line 37
    invoke-virtual/range {p1 .. p1}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v16

    .line 38
    .local v16, "packageManager":Landroid/content/pm/PackageManager;
    invoke-virtual/range {v16 .. v16}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v17

    const-string v18, "mPM"

    invoke-virtual/range {v17 .. v18}, Ljava/lang/Class;->getDeclaredField(Ljava/lang/String;)Ljava/lang/reflect/Field;

    move-result-object v8

    .line 39
    .local v8, "declaredField2":Ljava/lang/reflect/Field;
    const/16 v17, 0x1

    move/from16 v0, v17

    invoke-virtual {v8, v0}, Ljava/lang/reflect/Field;->setAccessible(Z)V

    .line 40
    move-object/from16 v0, v16

    invoke-virtual {v8, v0, v14}, Ljava/lang/reflect/Field;->set(Ljava/lang/Object;Ljava/lang/Object;)V

    .line 41
    sget-object v17, Ljava/lang/System;->out:Ljava/io/PrintStream;

    const-string v18, "PmsHook success."

    invoke-virtual/range {v17 .. v18}, Ljava/io/PrintStream;->println(Ljava/lang/String;)V
    :try_end_a1
    .catch Ljava/lang/Exception; {:try_start_2 .. :try_end_a1} :catch_f0

    .line 44
    :try_start_a1
    const-string v17, "android.common.HwFrameworkFactory"

    invoke-static/range {v17 .. v17}, Ljava/lang/Class;->forName(Ljava/lang/String;)Ljava/lang/Class;

    move-result-object v6

    .line 45
    .local v6, "cls3":Ljava/lang/Class;
    const-string v17, "getHwApiCacheManagerEx"

    const/16 v18, 0x0

    move/from16 v0, v18

    new-array v0, v0, [Ljava/lang/Class;

    move-object/from16 v18, v0

    move-object/from16 v0, v17

    move-object/from16 v1, v18

    invoke-virtual {v6, v0, v1}, Ljava/lang/Class;->getDeclaredMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v17

    const/16 v18, 0x0

    move/from16 v0, v18

    new-array v0, v0, [Ljava/lang/Object;

    move-object/from16 v18, v0

    move-object/from16 v0, v17

    move-object/from16 v1, v18

    invoke-virtual {v0, v6, v1}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v13

    .line 46
    .local v13, "invoke2":Ljava/lang/Object;
    invoke-virtual {v13}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v17

    const-string v18, "sPackageInfoCache"

    invoke-virtual/range {v17 .. v18}, Ljava/lang/Class;->getDeclaredField(Ljava/lang/String;)Ljava/lang/reflect/Field;

    move-result-object v9

    .line 47
    .local v9, "declaredField3":Ljava/lang/reflect/Field;
    const/16 v17, 0x1

    move/from16 v0, v17

    invoke-virtual {v9, v0}, Ljava/lang/reflect/Field;->setAccessible(Z)V

    .line 48
    invoke-virtual {v9, v13}, Ljava/lang/reflect/Field;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v11

    check-cast v11, Ljava/util/HashMap;

    .line 49
    .local v11, "hashMap":Ljava/util/HashMap;
    invoke-virtual {v11}, Ljava/util/HashMap;->clear()V

    .line 50
    invoke-virtual {v9, v13, v11}, Ljava/lang/reflect/Field;->set(Ljava/lang/Object;Ljava/lang/Object;)V
    :try_end_e6
    .catch Ljava/lang/Exception; {:try_start_a1 .. :try_end_e6} :catch_e7

    .line 58
    .end local v3    # "bArr":[[B
    .end local v4    # "cls":Ljava/lang/Class;
    .end local v5    # "cls2":Ljava/lang/Class;
    .end local v6    # "cls3":Ljava/lang/Class;
    .end local v7    # "declaredField":Ljava/lang/reflect/Field;
    .end local v8    # "declaredField2":Ljava/lang/reflect/Field;
    .end local v9    # "declaredField3":Ljava/lang/reflect/Field;
    .end local v11    # "hashMap":Ljava/util/HashMap;
    .end local v12    # "invoke":Ljava/lang/Object;
    .end local v13    # "invoke2":Ljava/lang/Object;
    .end local v14    # "newProxyInstance":Ljava/lang/Object;
    .end local v15    # "obj":Ljava/lang/Object;
    .end local v16    # "packageManager":Landroid/content/pm/PackageManager;
    :goto_e6
    return-void

    .line 51
    .restart local v3    # "bArr":[[B
    .restart local v4    # "cls":Ljava/lang/Class;
    .restart local v5    # "cls2":Ljava/lang/Class;
    .restart local v7    # "declaredField":Ljava/lang/reflect/Field;
    .restart local v8    # "declaredField2":Ljava/lang/reflect/Field;
    .restart local v12    # "invoke":Ljava/lang/Object;
    .restart local v14    # "newProxyInstance":Ljava/lang/Object;
    .restart local v15    # "obj":Ljava/lang/Object;
    .restart local v16    # "packageManager":Landroid/content/pm/PackageManager;
    :catch_e7
    move-exception v10

    .line 52
    .local v10, "e":Ljava/lang/Exception;
    :try_start_e8
    sget-object v17, Ljava/lang/System;->err:Ljava/io/PrintStream;

    const-string v18, "HwFramework PmsHook failed."

    invoke-virtual/range {v17 .. v18}, Ljava/io/PrintStream;->println(Ljava/lang/String;)V
    :try_end_ef
    .catch Ljava/lang/Exception; {:try_start_e8 .. :try_end_ef} :catch_f0

    goto :goto_e6

    .line 54
    .end local v3    # "bArr":[[B
    .end local v4    # "cls":Ljava/lang/Class;
    .end local v5    # "cls2":Ljava/lang/Class;
    .end local v7    # "declaredField":Ljava/lang/reflect/Field;
    .end local v8    # "declaredField2":Ljava/lang/reflect/Field;
    .end local v10    # "e":Ljava/lang/Exception;
    .end local v12    # "invoke":Ljava/lang/Object;
    .end local v14    # "newProxyInstance":Ljava/lang/Object;
    .end local v15    # "obj":Ljava/lang/Object;
    .end local v16    # "packageManager":Landroid/content/pm/PackageManager;
    :catch_f0
    move-exception v10

    .line 55
    .restart local v10    # "e":Ljava/lang/Exception;
    sget-object v17, Ljava/lang/System;->err:Ljava/io/PrintStream;

    const-string v18, "PmsHook failed."

    invoke-virtual/range {v17 .. v18}, Ljava/io/PrintStream;->println(Ljava/lang/String;)V

    .line 56
    invoke-virtual {v10}, Ljava/lang/Exception;->printStackTrace()V

    goto :goto_e6
.end method


# virtual methods
.method public attachBaseContext(Landroid/content/Context;)V
    .registers 2
    .param p1, "context"    # Landroid/content/Context;

    .prologue
    .line 62
    invoke-direct {p0, p1}, Lxyz/NoSignApplication;->hook(Landroid/content/Context;)V

    .line 63
    invoke-super {p0, p1}, Landroid/app/Application;->attachBaseContext(Landroid/content/Context;)V

    .line 64
    return-void
.end method

.method public invoke(Ljava/lang/Object;Ljava/lang/reflect/Method;[Ljava/lang/Object;)Ljava/lang/Object;
    .registers 10
    .param p1, "obj"    # Ljava/lang/Object;
    .param p2, "method"    # Ljava/lang/reflect/Method;
    .param p3, "objArr"    # [Ljava/lang/Object;
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/Throwable;
        }
    .end annotation

    .prologue
    .line 67
    const-string v3, "getPackageInfo"

    invoke-virtual {p2}, Ljava/lang/reflect/Method;->getName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-eqz v3, :cond_4b

    .line 68
    const/4 v3, 0x0

    aget-object v2, p3, v3

    check-cast v2, Ljava/lang/String;

    .line 69
    .local v2, "str":Ljava/lang/String;
    const/4 v3, 0x1

    aget-object v3, p3, v3

    check-cast v3, Ljava/lang/Integer;

    invoke-virtual {v3}, Ljava/lang/Integer;->intValue()I

    move-result v3

    and-int/lit8 v3, v3, 0x40

    if-eqz v3, :cond_4b

    iget-object v3, p0, Lxyz/NoSignApplication;->appPkgName:Ljava/lang/String;

    invoke-virtual {v3, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-eqz v3, :cond_4b

    .line 70
    iget-object v3, p0, Lxyz/NoSignApplication;->base:Ljava/lang/Object;

    invoke-virtual {p2, v3, p3}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/content/pm/PackageInfo;

    .line 71
    .local v1, "packageInfo":Landroid/content/pm/PackageInfo;
    iget-object v3, p0, Lxyz/NoSignApplication;->sign:[[B

    array-length v3, v3

    new-array v3, v3, [Landroid/content/pm/Signature;

    iput-object v3, v1, Landroid/content/pm/PackageInfo;->signatures:[Landroid/content/pm/Signature;

    .line 72
    const/4 v0, 0x0

    .local v0, "i":I
    :goto_36
    iget-object v3, v1, Landroid/content/pm/PackageInfo;->signatures:[Landroid/content/pm/Signature;

    array-length v3, v3

    if-ge v0, v3, :cond_51

    .line 73
    iget-object v3, v1, Landroid/content/pm/PackageInfo;->signatures:[Landroid/content/pm/Signature;

    new-instance v4, Landroid/content/pm/Signature;

    iget-object v5, p0, Lxyz/NoSignApplication;->sign:[[B

    aget-object v5, v5, v0

    invoke-direct {v4, v5}, Landroid/content/pm/Signature;-><init>([B)V

    aput-object v4, v3, v0

    .line 72
    add-int/lit8 v0, v0, 0x1

    goto :goto_36

    .line 78
    .end local v0    # "i":I
    .end local v1    # "packageInfo":Landroid/content/pm/PackageInfo;
    .end local v2    # "str":Ljava/lang/String;
    :cond_4b
    iget-object v3, p0, Lxyz/NoSignApplication;->base:Ljava/lang/Object;

    invoke-virtual {p2, v3, p3}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    :cond_51
    return-object v1
.end method
